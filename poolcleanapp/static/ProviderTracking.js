function initializeTasks(tasks) {
  const tasksContainer = document.getElementById("tasksContainer");
  tasks.forEach((task) => {
    const taskElement = createTaskElement(task);
    tasksContainer.appendChild(taskElement);
  });

  // Create and show the "Finish" button regardless of task completion status
  const buttonContainer = document.createElement("div");
  buttonContainer.classList.add("button-container");

  const newButton = document.createElement("button");
  newButton.textContent = "Finish";
  newButton.classList.add("btn", "btn-primary");

  buttonContainer.appendChild(newButton);
  tasksContainer.appendChild(buttonContainer);

  // Event listener for the "Finish" button
  newButton.addEventListener("click", function () {
    // Check if any tasks are not completed
    const anyTaskIncomplete = tasks.some((task) => task.status !== "y");

    if (anyTaskIncomplete) {
      // If there are incomplete tasks, show the popup
      showPopup();
    } else {
      // If all tasks are completed, you might want to show a different message or take some other action
      console.log("All tasks are complete. No action needed.");
    }
  });
}

function createTaskElement(task) {
  const taskElement = document.createElement("div");
  taskElement.classList.add(
    "mt-2",
    "task",
    "d-flex",
    "flex-column",
    "justify-content-between"
  );

  const taskTitle = document.createElement("div");
  taskTitle.classList.add(
    "d-flex",
    "justify-content-between",
    "task-title",
    "align-items-center"
  );
  taskTitle.innerHTML = `<b>${task.name}</b>`;
  taskElement.appendChild(taskTitle);

  const taskDesc = document.createElement("div");
  taskDesc.classList.add(
    "d-flex",
    "justify-content-between",
    "align-items-center"
  );
  taskDesc.style.display = "none";

  const detailsButton = document.createElement("button");
  detailsButton.classList.add("btn", "btn-info", "dropdown-toggle", "ms-1");
  detailsButton.textContent = "Details";
  taskTitle.appendChild(detailsButton);

  detailsButton.onclick = function () {
    taskDesc.style.display =
      taskDesc.style.display === "none" ? "block" : "none";
    taskDesc.innerHTML =
      taskDesc.style.display === "block" ? task.description : "";
  };

  taskElement.appendChild(taskDesc);

  const taskStatus = document.createElement("div");
  taskStatus.classList.add("d-flex", "justify-content-end");
  taskStatus.textContent =
    task.status === "y" ? "✔ Completed" : "✖ Not Yet Complete";
  taskStatus.className +=
    task.status === "y" ? " task-status-complete" : " task-status-incomplete";
  taskElement.appendChild(taskStatus);

  if (task.status !== "y") {
    const completeButton = document.createElement("button");
    completeButton.classList.add("btn", "btn-success", "ms-1");
    completeButton.textContent = "Mark as Complete";
    taskElement.appendChild(completeButton);

    completeButton.addEventListener("click", function () {
      task.status = "y";
      taskStatus.className = "d-flex justify-content-end task-status-complete";
      taskStatus.textContent = "✔ Completed";

      const timeStamp = new Date().toLocaleTimeString();
      const timeStampElement = document.createElement("span");
      timeStampElement.textContent = ` - Completed at ${timeStamp}`;
      taskStatus.appendChild(timeStampElement);

      completeButton.style.display = "none";
    });
  }

  return taskElement;
}

function showPopup() {
  const overlay = document.createElement("div");
  overlay.classList.add("overlay");

  const popup = document.createElement("div");
  popup.classList.add("popup");

  const messageContainer = document.createElement("div");
  messageContainer.textContent = "Some task are not complete.";
  messageContainer.style.textAlign = "center";

  // Create the buttons container
  const buttonsContainer = document.createElement("div");
  buttonsContainer.style.display = "flex";
  buttonsContainer.style.justifyContent = "center"; // Center the buttons
  buttonsContainer.style.gap = "10px"; // Add gap between buttons

  // Create the close button
  const closeButton = document.createElement("button");
  closeButton.textContent = "Close";
  closeButton.classList.add("popup-close-btn");

  // Create the finish button
  const finishButton = document.createElement("button");
  finishButton.textContent = "Finish";
  finishButton.classList.add("popup-open-btn"); // Use the same class for styling

  // Append buttons to the buttons container
  buttonsContainer.appendChild(closeButton);
  buttonsContainer.appendChild(finishButton);

  // Append the message container and buttons container to the popup
  popup.appendChild(messageContainer);
  popup.appendChild(buttonsContainer);

  document.body.appendChild(overlay);
  document.body.appendChild(popup);

  closeButton.addEventListener("click", function () {
    popup.remove();
    overlay.remove();
  });

  finishButton.addEventListener("click", function () {
    console.log("Finish button clicked");
    popup.remove();
    overlay.remove();
  });
}
