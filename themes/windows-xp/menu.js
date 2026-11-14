"use strict";

const start = document.querySelector(".start");
document.addEventListener("click", (event) => {
  if (!start.contains(event.target) || event.target.closest("a")) start.open = false;
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && start.open) {
    start.open = false;
    start.querySelector("summary").focus();
  }
});
