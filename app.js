(function () {
  const menuButton = document.getElementById("menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");
  const submitButton = document.getElementById("submit-btn");
  const status = document.getElementById("form-status");
  const form = document.querySelector(".contact-form");

  if (menuButton && mobileMenu) {
    menuButton.addEventListener("click", function () {
      const expanded = menuButton.getAttribute("aria-expanded") === "true";
      menuButton.setAttribute("aria-expanded", String(!expanded));
      mobileMenu.classList.toggle("open", !expanded);
      menuButton.textContent = expanded ? "Menu" : "Close";
    });

    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menuButton.setAttribute("aria-expanded", "false");
        mobileMenu.classList.remove("open");
        menuButton.textContent = "Menu";
      });
    });
  }

  if (form && status && submitButton) {
    form.addEventListener("submit", function () {
      submitButton.disabled = true;
      submitButton.textContent = "Sending...";
      setTimeout(function () {
        status.textContent = "Thanks. Your inquiry is queued. We will respond within one business day.";
        submitButton.disabled = false;
        submitButton.textContent = "Send Inquiry";
        form.reset();
      }, 600);
    });
  }

  const sections = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.14 }
    );

    sections.forEach(function (item) {
      observer.observe(item);
    });
  } else {
    sections.forEach(function (item) {
      item.classList.add("in-view");
    });
  }
})();
