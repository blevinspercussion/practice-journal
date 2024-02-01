let practiceItems = document.querySelectorAll(".practice-item");

for (let i = 0; i < practiceItems.length; i++) {
  practiceItems[i].addEventListener("click", () => {
    practiceItems[i].classList.contains("completed")
      ? practiceItems[i].classList.remove("completed")
      : practiceItems[i].classList.add("completed");
  });
}
