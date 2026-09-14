"use strict";

// Obfuscação para reduzir coleta estática; não é criptografia.
const contactCode = [124, 124, 120, 120, 112, 126, 120, 126, 113, 112, 126, 124, 126];

for (const button of document.querySelectorAll("[data-whatsapp]")) {
  button.addEventListener("click", () => {
    const destination = contactCode.map((value) => String.fromCharCode(value ^ 73)).join("");
    window.location.assign("https://wa.me/" + destination);
  });
  button.hidden = false;
}
