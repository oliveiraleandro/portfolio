"use strict";

// Both languages share section IDs. Keep the section when following a language link.
for (const link of document.querySelectorAll("[data-language-switch]")) {
  const destination = new URL(link.href);
  const updateHash = () => {
    destination.hash = window.location.hash;
    link.href = destination.href;
  };
  updateHash();
  window.addEventListener("hashchange", updateHash);
}
