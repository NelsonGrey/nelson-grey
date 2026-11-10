const http = require("http");
const fs = require("fs");
const path = require("path");

const preferredPort = Number(process.env.PORT || 4173);
const maxPortAttempts = 20;
const rootDir = fs.realpathSync(process.cwd());

const mimeTypes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".ico": "image/x-icon",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8"
};

function loadRedirects() {
  try {
    const config = JSON.parse(fs.readFileSync(path.join(rootDir, "firebase.json"), "utf8"));
    const redirects = config.hosting && config.hosting.redirects;
    return Array.isArray(redirects) ? redirects : [];
  } catch (err) {
    return [];
  }
}

const redirects = loadRedirects();

function matchRedirect(pathname) {
  for (const rule of redirects) {
    const names = [];
    const source = String(rule.source || "");
    const pattern = source
      .replace(/[.+?^${}()|[\]\\]/g, "\\$&")
      .replace(/\\\*\\\*/g, ".*")
      .replace(/\\\*/g, "[^/]*")
      .replace(/:([A-Za-z0-9_]+)/g, function (_, name) {
        names.push(name);
        return "([^/]+)";
      });
    const match = pathname.match(new RegExp("^" + pattern + "$"));
    if (!match) continue;
    let destination = String(rule.destination || "/");
    names.forEach(function (name, index) {
      destination = destination.replace(":" + name, match[index + 1]);
    });
    return { destination: destination, type: Number(rule.type) || 301 };
  }
  return null;
}

function cleanUrlRedirect(pathname) {
  if (pathname.length > 1 && pathname.endsWith("/")) {
    return pathname.replace(/\/+$/, "") || "/";
  }
  if (pathname === "/index.html" || pathname.endsWith("/index.html")) {
    const parent = pathname.slice(0, -"/index.html".length);
    return parent || "/";
  }
  if (pathname.endsWith(".html")) {
    return pathname.slice(0, -".html".length) || "/";
  }
  return null;
}

function insideRoot(filePath) {
  const resolved = path.resolve(filePath);
  return resolved === rootDir || resolved.startsWith(rootDir + path.sep);
}

function resolveFile(pathname) {
  let rel = pathname.replace(/^\/+/, "");
  if (rel.includes("\0")) return null;
  if (rel === "") rel = "index.html";
  const normalized = path.normalize(rel);
  if (normalized.startsWith("..") || path.isAbsolute(normalized)) return null;
  let candidate = path.join(rootDir, normalized);
  if (!insideRoot(candidate)) return null;

  if (fs.existsSync(candidate) && fs.statSync(candidate).isDirectory()) {
    candidate = path.join(candidate, "index.html");
  } else if (!fs.existsSync(candidate)) {
    const htmlCandidate = candidate + ".html";
    if (fs.existsSync(htmlCandidate)) candidate = htmlCandidate;
  }

  if (!fs.existsSync(candidate) || !fs.statSync(candidate).isFile()) return null;
  const real = fs.realpathSync(candidate);
  if (!insideRoot(real)) return null;
  return real;
}

function sendRedirect(res, location, status) {
  res.writeHead(status, {
    Location: location,
    "Content-Type": "text/plain; charset=utf-8"
  });
  res.end("Redirecting to " + location);
}

function send404(res) {
  const filePath = path.join(rootDir, "404.html");
  fs.readFile(filePath, function (err, data) {
    if (err) {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Not found");
      return;
    }
    res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
    res.end(data);
  });
}

function sendFile(res, filePath) {
  const ext = path.extname(filePath).toLowerCase();
  fs.readFile(filePath, function (err, data) {
    if (err) {
      send404(res);
      return;
    }
    res.writeHead(200, { "Content-Type": mimeTypes[ext] || "application/octet-stream" });
    res.end(data);
  });
}

const server = http.createServer(function (req, res) {
  const requestUrl = new URL(req.url || "/", "http://127.0.0.1");
  let pathname = decodeURIComponent(requestUrl.pathname);
  const query = requestUrl.search || "";

  if (pathname.includes("\0")) {
    send404(res);
    return;
  }

  const cleaned = cleanUrlRedirect(pathname) || pathname;
  const redirect = matchRedirect(cleaned) || matchRedirect(pathname);
  if (redirect) {
    const joiner = redirect.destination.includes("?") ? "" : query;
    sendRedirect(res, redirect.destination + joiner, redirect.type);
    return;
  }
  if (cleaned !== pathname) {
    sendRedirect(res, cleaned + query, 301);
    return;
  }

  const filePath = resolveFile(pathname);
  if (!filePath) {
    send404(res);
    return;
  }
  sendFile(res, filePath);
});

let activePort = preferredPort;
let attempts = 0;

function startServer() {
  server.listen(activePort, "127.0.0.1", function () {
    console.log("Nelson Grey site running at http://127.0.0.1:" + activePort);
  });
}

server.on("error", function (err) {
  if (err && err.code === "EADDRINUSE" && attempts < maxPortAttempts) {
    attempts += 1;
    activePort += 1;
    console.warn(
      "Port " + (activePort - 1) + " is in use. Retrying on http://127.0.0.1:" + activePort + " ..."
    );
    setTimeout(startServer, 50);
    return;
  }

  console.error("Failed to start dev server:", err && err.message ? err.message : err);
  process.exit(1);
});

startServer();
