function updateLiveDate() {
  const dateElement = document.getElementById("liveDate");
  const now = new Date();
  const options = { weekday: "long", month: "long", day: "numeric" };
  dateElement.textContent = now.toLocaleDateString("en-US", options);
}

// Call the function to update the date when the script loads
updateLiveDate();

document.addEventListener("DOMContentLoaded", function () {
  // Initially hide all completion prompts
  const allPrompts = document.querySelectorAll(".text-end");
  allPrompts.forEach(function (prompt) {
    prompt.style.display = "none";
  });

  // Show the first prompt
  if (allPrompts.length > 0) {
    allPrompts[0].style.display = "";
  }

  document.addEventListener("click", function (event) {
    // Check if the clicked element is a complete or not-complete button
    if (
      event.target.classList.contains("complete") ||
      event.target.classList.contains("not-complete")
    ) {
      const taskStatusContainer = event.target
        .closest(".task")
        .querySelector(".text-end");

      // Update the task status
      const statusMessage = event.target.classList.contains("complete")
        ? "Complete"
        : "Not Complete";
      const statusClass = event.target.classList.contains("complete")
        ? "task-status-complete"
        : "task-status-not-complete";
      updateTaskStatus(taskStatusContainer, statusMessage, statusClass);

      // Show the next prompt, if any
      const nextPrompt = getNextPrompt(taskStatusContainer);
      if (nextPrompt) {
        nextPrompt.style.display = "";
      }
    }
  });
});

function updateTaskStatus(taskStatusContainer, statusMessage, statusClass) {
  // Remove the current content in the task status container
  taskStatusContainer.innerHTML = "";

  // Create and add the status message
  const statusElement = document.createElement("p");
  statusElement.textContent = statusMessage;
  statusElement.className = statusClass; // Use the class for styling
  taskStatusContainer.appendChild(statusElement); // Add the status message
}

function getNextPrompt(currentPrompt) {
  const allPrompts = Array.from(document.querySelectorAll(".text-end"));
  const currentIndex = allPrompts.indexOf(currentPrompt);
  return allPrompts[currentIndex + 1]; // Returns undefined if there is no next prompt, which is fine
}


