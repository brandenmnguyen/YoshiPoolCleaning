// Inside your client-side JavaScript file (e.g., clienttracking.js)

const ws_scheme = window.location.protocol === "https:" ? "wss://" : "ws://";
const socket = new WebSocket(ws_scheme + window.location.host + '/ws/clienttracking/');

socket.onmessage = function(event) {
  const data = JSON.parse(event.data);
  if (data.type === 'task_update') {
      const task = data.task;
      const taskElement = document.getElementById(`task-${task.id}`);
      if (taskElement) {
          const taskStatus = taskElement.querySelector('.task-status');
          taskStatus.textContent = task.status === "y" ? "✔ Completed" : "✖ Not Yet Complete";
          taskStatus.className = task.status === "y" ? "task-status-complete" : "task-status-incomplete";
      } else {
          // If the task doesn't exist in the DOM, you might want to add it
          const newTaskElement = createTaskElement(task);
          document.getElementById("tasksContainer").appendChild(newTaskElement);
      }
  }
};


function createTaskElement(task) {
  const taskElement = document.createElement("div");
  taskElement.classList.add("task");
  taskElement.id = `task-${task.pk}`;

  const taskName = document.createElement("div");
  taskName.classList.add("task-name");
  taskName.textContent = task.name;

  const taskDesc = document.createElement("div");
  taskDesc.classList.add("task-desc");
  taskDesc.textContent = task.description;

  const taskStatus = document.createElement("div");
  taskStatus.classList.add("task-status");
  taskStatus.textContent = task.status === "y" ? "✔ Completed" : "✖ Not Yet Complete";
  taskStatus.className = task.status === "y" ? "task-status-complete" : "task-status-incomplete";

  taskElement.appendChild(taskName);
  taskElement.appendChild(taskDesc);
  taskElement.appendChild(taskStatus);

  return taskElement;
}

// Function to show popup
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
