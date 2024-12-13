// scroll.js
document.addEventListener("DOMContentLoaded", function () {
  var scrollUpButton = document.createElement("button");
  scrollUpButton.innerText = "↑";
  scrollUpButton.className = "scroll-button scroll-up";
  document.body.appendChild(scrollUpButton);

  var scrollDownButton = document.createElement("button");
  scrollDownButton.innerText = "↓";
  scrollDownButton.className = "scroll-button scroll-down";
  document.body.appendChild(scrollDownButton);

  scrollUpButton.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  scrollDownButton.addEventListener("click", function () {
    window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
  });

  window.addEventListener("scroll", function () {
    if (window.scrollY > 100) {
      scrollUpButton.style.display = "block";
    } else {
      scrollUpButton.style.display = "none";
    }
  });

  scrollDownButton.style.display = "block";
});
