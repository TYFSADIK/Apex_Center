/* Apex Collision Center - interactions */
(function () {
  "use strict";

  /* Mobile nav */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }

  /* FAQ accordion */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.addEventListener("click", function () {
      var isOpen = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach(function (other) {
        other.classList.remove("open");
        other.querySelector(".faq-a").style.maxHeight = null;
        other.querySelector(".faq-q").setAttribute("aria-expanded", "false");
      });
      if (!isOpen) {
        item.classList.add("open");
        a.style.maxHeight = a.scrollHeight + "px";
        q.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* Scroll reveal */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("visible"); });
  }

  /* Highlight today's hours row */
  var day = new Date().getDay(); /* 0 Sun .. 6 Sat */
  document.querySelectorAll(".hours-table tr[data-day]").forEach(function (row) {
    if (parseInt(row.getAttribute("data-day"), 10) === day) row.classList.add("today");
  });

  /* Open/closed badge in topbar */
  var badge = document.getElementById("open-badge");
  if (badge) {
    var now = new Date();
    var d = now.getDay();
    var mins = now.getHours() * 60 + now.getMinutes();
    var open = (d >= 1 && d <= 5 && mins >= 540 && mins < 1020) || (d === 6 && mins >= 600 && mins < 900);
    badge.querySelector(".dot").classList.toggle("closed", !open);
    badge.querySelector(".open-text").textContent = open ? "Open now" : "Currently closed";
  }

  /* Booking form -> composes an email to the shop */
  var form = document.getElementById("booking-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var get = function (id) {
        var el = document.getElementById(id);
        return el ? el.value.trim() : "";
      };
      var subject = "Service booking request: " + get("bf-service") + " (" + get("bf-name") + ")";
      var body = [
        "Name: " + get("bf-name"),
        "Phone: " + get("bf-phone"),
        "Email: " + get("bf-email"),
        "Vehicle: " + get("bf-year") + " " + get("bf-make") + " " + get("bf-model"),
        "Service needed: " + get("bf-service"),
        "Preferred date: " + get("bf-date"),
        "Preferred time: " + get("bf-time"),
        "",
        "Details:",
        get("bf-notes")
      ].join("\n");
      window.location.href =
        "mailto:mustafa@apexcollisioncenter.ca?subject=" +
        encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
      var note = document.getElementById("booking-note");
      if (note) note.hidden = false;
    });
  }

  /* Footer year */
  document.querySelectorAll(".js-year").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
