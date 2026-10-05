(function () {
  var GTM_ID = "GTM-N7NQ6PMN";
  var STORAGE_KEY = "ng-consent";

  window.dataLayer = window.dataLayer || [];

  function loadGTM() {
    if (window.__gtmLoaded) return;
    window.__gtmLoaded = true;

    window.dataLayer.push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
    var script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM_ID;
    var firstScript = document.getElementsByTagName("script")[0];
    firstScript.parentNode.insertBefore(script, firstScript);

    function insertGTMFrame() {
      if (!document.body || document.getElementById("gtm-consent-frame")) return;
      var iframe = document.createElement("iframe");
      iframe.id = "gtm-consent-frame";
      iframe.src = "https://www.googletagmanager.com/ns.html?id=" + GTM_ID;
      iframe.height = 0;
      iframe.width = 0;
      iframe.style.display = "none";
      iframe.style.visibility = "hidden";
      document.body.insertBefore(iframe, document.body.firstChild);
    }

    if (document.body) {
      insertGTMFrame();
    } else {
      document.addEventListener("DOMContentLoaded", insertGTMFrame, { once: true });
    }
  }

  function getConsent() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setConsent(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (e) {}
  }

  var consent = getConsent();
  if (consent === "granted") {
    loadGTM();
  }

  document.addEventListener("DOMContentLoaded", function () {
    var banner = document.getElementById("cookie-consent");
    var acceptBtn = document.getElementById("cookie-accept");
    var declineBtn = document.getElementById("cookie-decline");

    if (banner && consent !== "granted" && consent !== "denied") {
      banner.hidden = false;
    }

    if (acceptBtn) {
      acceptBtn.addEventListener("click", function () {
        setConsent("granted");
        if (banner) banner.hidden = true;
        loadGTM();
      });
    }

    if (declineBtn) {
      declineBtn.addEventListener("click", function () {
        setConsent("denied");
        if (banner) banner.hidden = true;
      });
    }

    var resetBtn = document.getElementById("cookie-manage");
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        try {
          window.localStorage.removeItem(STORAGE_KEY);
        } catch (e) {}
        window.location.reload();
      });
    }
  });
})();
