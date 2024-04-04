
/*document.addEventListener('DOMContentLoaded', function () {
  // Adjust the URL as necessary
  const wsStart = window.location.protocol === "https:" ? "wss://" : "ws://";
  const wsPath = wsStart + window.location.host + "/ws/provider-status-update/"; // General path, adjust as necessary
  const taskStatusSocket = new WebSocket(wsPath);

  window.sendStatusUpdate = function(taskId, statusUpdate) {
      taskStatusSocket.send(JSON.stringify({
          taskId: taskId,
          status: statusUpdate
      }));
  };

  taskStatusSocket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      console.log('Message from server: ', data);
      // Handle incoming messages, such as confirmation of status update
  };

  taskStatusSocket.onclose = function(e) {
      console.error('Task status socket closed unexpectedly');
  };

  taskStatusSocket.onerror = function(err) {
      console.error('WebSocket error: ', err);
  };
});*/
//--------------
console.log("javascript is running");
  // When the DOM is fully loaded
  document.addEventListener('DOMContentLoaded', (event) => {
    // Get all the update status forms
    document.querySelectorAll('.update-status-form').forEach(form => {
      // Add an event listener to each form
      form.addEventListener('submit', function(e) {
        // Prevent the default form submission
        e.preventDefault();

        // Get the task id from the data-task-id attribute
        const taskId = this.getAttribute('data-task-id');

        // Show the updated at information for the right task
        document.getElementById('updated-at-' + taskId).style.display = 'block';

        // You can now submit the form using AJAX or the following line to submit traditionally
        // this.submit();
      });
    });
  });
//-------------------------------------------------------------------
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
