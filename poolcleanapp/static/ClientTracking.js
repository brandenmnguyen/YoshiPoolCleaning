function updateLiveDate() {
  const dateElement = document.getElementById("liveDate");
  const now = new Date();
  const options = { weekday: "long", month: "long", day: "numeric" };
  dateElement.textContent = now.toLocaleDateString("en-US", options);
}

// Call the function to update the date when the script loads
updateLiveDate();

const technicianDetails = {
  name: "Robert",
  status: "Arrived",
};

// Define your array with task details
// Define your array with task details
const tasks = [
  { title: "Vacuuming", time: "9:00 AM", status: "Complete" },
  { title: "Chemical Balancing", time: "10:00 AM", status: "Complete" },
  { title: "Mopping", time: "11:00 AM", status: "Complete" },
];

function updateTechnicianDetails() {
  // Get the elements by their class names
  const nameElement = document.querySelector(".name-text");
  const statusElement = document.querySelector(".status-arrived");

  // Update the text content of the elements
  nameElement.textContent = technicianDetails.name;
  statusElement.textContent = technicianDetails.status;

  // Optionally, add logic to change the class based on the status
  // For example, if you have different classes for different statuses:
  statusElement.className = ""; // Clear previous classes
  statusElement.classList.add("status-arrived"); // Add the class back if needed
  if (technicianDetails.status.toLowerCase() === "arrived") {
    statusElement.classList.add("text-success"); // Example class for positive status
  } else {
    statusElement.classList.add("text-danger"); // Example class for negative status
  }
}

document.addEventListener("DOMContentLoaded", function () {
  insertTaskData(); // Existing function to insert task data
  updateTechnicianDetails(); // New function to update technician details
});

function createTaskElement(task) {
  const taskDiv = document.createElement("div");
  taskDiv.classList.add(
    "task",
    "d-flex",
    "flex-column",
    "justify-content-between",
    "mt-3"
  );

  const titleDiv = document.createElement("div");
  titleDiv.classList.add("d-flex", "justify-content-between");

  const taskTitleDiv = document.createElement("div");
  taskTitleDiv.classList.add("task-title", "d-flex", "align-items-center");

  const titleText = document.createTextNode(task.title);
  taskTitleDiv.appendChild(titleText);

  const dropdownButton = document.createElement("button");
  dropdownButton.classList.add("dropdown-toggle", "ms-1");
  taskTitleDiv.appendChild(dropdownButton);

  const taskTimeDiv = document.createElement("div");
  taskTimeDiv.classList.add("task-time");
  taskTimeDiv.textContent = task.time;

  titleDiv.appendChild(taskTitleDiv);
  titleDiv.appendChild(taskTimeDiv);

  const statusDiv = document.createElement("div");
  statusDiv.classList.add("d-flex", "justify-content-end");

  const taskStatusDiv = document.createElement("div");
  taskStatusDiv.classList.add("task-status");
  taskStatusDiv.textContent = task.status;

  // Add class based on status
  if (task.status === "Complete") {
    taskStatusDiv.classList.add("status-complete");
  } else if (task.status === "In Progress") {
    taskStatusDiv.classList.add("status-in-progress");
  }
  // Add more conditions as needed for other statuses

  statusDiv.appendChild(taskStatusDiv);

  taskDiv.appendChild(titleDiv);
  taskDiv.appendChild(statusDiv);

  return taskDiv;
}

function insertAllTaskData() {
  const tasksContainer = document.querySelector(".tasks-container");
  tasksContainer.innerHTML = ""; // Clear existing tasks

  tasks.forEach((task) => {
    const taskElement = createTaskElement(task);
    tasksContainer.appendChild(taskElement);
  });
}

document.addEventListener("DOMContentLoaded", function () {
  insertAllTaskData(); // Insert all tasks when the document is ready
  updateTechnicianDetails(); // Existing function to update technician details
});
