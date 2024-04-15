function createTaskElement(task) {
  // Create task element
  const taskElement = document.createElement("div");
  taskElement.classList.add(
    "mt-2",
    "task",
    "d-flex",
    "flex-column",
    "justify-content-between"
  );

  // Task title
  const taskTitle = document.createElement("div");
  taskTitle.classList.add(
    "d-flex",
    "justify-content-between",
    "task-title",
    "align-items-center"
  );
  taskTitle.innerHTML = `<b>${task.name}</b>`;
  taskElement.appendChild(taskTitle);

  // Task description (initially hidden)
  const taskDesc = document.createElement("div");
  taskDesc.classList.add(
    "d-flex",
    "justify-content-between",
    "align-items-center"
  );
  taskDesc.style.display = "none"; // Initially hide the description

  // Button to toggle description visibility
  const detailsButton = document.createElement("button");
  detailsButton.classList.add("btn", "btn-info", "dropdown-toggle", "ms-1"); // Add Bootstrap classes for styling
  detailsButton.textContent = "Details";
  taskTitle.appendChild(detailsButton);

  detailsButton.onclick = function () {
    taskDesc.style.display =
      taskDesc.style.display === "none" ? "block" : "none";
    taskDesc.innerHTML =
      taskDesc.style.display === "block" ? task.description : "";
  };

  // Append description to task element (it will be toggled by the details button)
  taskElement.appendChild(taskDesc);

  // Task status
  const taskStatus = document.createElement("div");
  taskStatus.classList.add("d-flex", "justify-content-end");
  taskStatus.textContent =
    task.status === "y" ? "✔ Completed" : "✖ Not Yet Complete";
  taskStatus.className +=
    task.status === "y" ? " task-status-complete" : " task-status-incomplete";
  taskElement.appendChild(taskStatus);

  return taskElement;
}
