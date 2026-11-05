"use strict";

const siteHeader = document.querySelector(".site-header");

if (siteHeader) {
  let updatePending = false;

  function updateHeader() {
    siteHeader.classList.toggle("is-scrolled", window.scrollY > 24);
    updatePending = false;
  }

  window.addEventListener("scroll", () => {
    if (!updatePending) {
      updatePending = true;
      window.requestAnimationFrame(updateHeader);
    }
  }, { passive: true });

  window.addEventListener("pageshow", updateHeader);
  updateHeader();
}
