// Handle main menu

let navMenu = document.getElementById("nav-menu");
let menuButton = document.getElementById("hamburger-div");

menuButton.addEventListener("click", () => {
  if (navMenu.style.visibility == "visible") {
    navMenu.style.visibility = "hidden";
  } else {
    navMenu.style.visibility = "visible";
  }
});

// Handle Practice Page

let practiceItems = document.querySelectorAll(".practice-item");

for (let i = 0; i < practiceItems.length; i++) {
  practiceItems[i].addEventListener("click", () => {
    practiceItems[i].classList.contains("completed")
      ? practiceItems[i].classList.remove("completed")
      : practiceItems[i].classList.add("completed");
  });
}
