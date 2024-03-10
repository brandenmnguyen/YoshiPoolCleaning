function initializeTasks(tasks) {
  const tasksContainer = document.getElementById("tasksContainer");
  tasks.forEach((task) => {
    const taskElement = createTaskElement(task);
    tasksContainer.appendChild(taskElement);
  });

  // Create a div to wrap the button and facilitate centering
  const buttonContainer = document.createElement("div");
  buttonContainer.classList.add("button-container");

  // Create the button
  const newButton = document.createElement("button");
  newButton.textContent = "Finish";
  newButton.classList.add("btn", "btn-primary");

  // Append the button to the buttonContainer, then append the buttonContainer to the tasksContainer
  buttonContainer.appendChild(newButton);
  tasksContainer.appendChild(buttonContainer);

  // Add an event listener to the newButton for click events
  newButton.addEventListener("click", function () {
    // Call the function to show the popup
    showPopup();
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