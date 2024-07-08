document.addEventListener("DOMContentLoaded", function() {
    // Create scroll buttons
    const scrollUpButton = document.createElement("button");
    const scrollDownButton = document.createElement("button");

    // Set button styles and content
    scrollUpButton.innerHTML = "⬆️";
    scrollDownButton.innerHTML = "⬇️";
    scrollUpButton.className = "scroll-button up";
    scrollDownButton.className = "scroll-button down";

    // Append buttons to the body
    document.body.appendChild(scrollUpButton);
    document.body.appendChild(scrollDownButton);

    // Add scroll functionality
    scrollUpButton.addEventListener("click", function() {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    scrollDownButton.addEventListener("click", function() {
        window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
    });
});
