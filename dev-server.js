const http = require("http");
const fs = require("fs");
const path = require("path");

const preferredPort = Number(process.env.PORT || 4173);
const maxPortAttempts = 20;
const rootDir = process.cwd();

const mimeTypes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".ico": "image/x-icon"
};

function resolvePath(urlPath) {
  const clean = decodeURIComponent((urlPath || "/").split("?")[0]);
  const requested = clean === "/" ? "/index.html" : clean;
  const safePath = path.normalize(requested).replace(/^([.][.][/\\])+/, "");
  return path.join(rootDir, safePath);
}

const server = http.createServer((req, res) => {
  const filePath = resolvePath(req.url || "/");

  fs.readFile(filePath, (err, data) => {
    if (!err) {
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200, { "Content-Type": mimeTypes[ext] || "application/octet-stream" });
      res.end(data);
      return;
    }

    const fallbackPath = path.join(rootDir, "index.html");
    fs.readFile(fallbackPath, (fallbackErr, fallbackData) => {
      if (fallbackErr) {
        res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
        res.end("Not found");
        return;
      }
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.end(fallbackData);
    });
  });
});

let activePort = preferredPort;
let attempts = 0;

function startServer() {
  server.listen(activePort, "127.0.0.1", () => {
    console.log(`Nelson Grey site running at http://127.0.0.1:${activePort}`);
  });
}

server.on("error", (err) => {
  if (err && err.code === "EADDRINUSE" && attempts < maxPortAttempts) {
    attempts += 1;
    activePort += 1;
    console.warn(
      `Port ${activePort - 1} is in use. Retrying on http://127.0.0.1:${activePort} ...`
    );
    setTimeout(startServer, 50);
    return;
  }

  console.error("Failed to start dev server:", err && err.message ? err.message : err);
  process.exit(1);
});

startServer();
