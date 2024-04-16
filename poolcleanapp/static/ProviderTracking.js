let globalCompanyId = null;  // Global scope variable for company ID
let globalClientId = null;  // Global scope variable for client ID
let globalTaskId = null;

document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('toggleTasksButton');
    var tasksContainer = document.getElementById('tasksContainer');

    toggleButton.onclick = function() {
        // Check current display style and toggle it
        if (tasksContainer.style.display === 'none') {
            tasksContainer.style.display = 'block';
            toggleButton.textContent = 'Minimize Tasks'; // Change button text to indicate action
        } else {
            tasksContainer.style.display = 'none';
            toggleButton.textContent = 'Display Tasks'; // Change back the button text
        }
    };
});

document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('toggleTasksButton');
    var tasksContainer = document.getElementById('tasksContainer');
    var arrowIcon = document.getElementById('arrowIcon');

    toggleButton.onclick = function() {
        if (tasksContainer.style.display === 'none') {
            tasksContainer.style.display = 'block';
            arrowIcon.style.transform = 'rotate(180deg)'; // Arrow points up
        } else {
            tasksContainer.style.display = 'none';
            arrowIcon.style.transform = 'rotate(0deg)'; // Arrow points down
        }
    };
});

function showTaskpingTab() {
    // Activate the 'nav-taskping-tab' tab
    var tabElement = document.getElementById('nav-taskping-tab');
    var newTab = new bootstrap.Tab(tabElement);
    newTab.show();
}

async function onAppointmentButtonClick(appointmentId) {
    try {
        // Fetch the details of the appointment
        const appointmentResponse = await fetch(`/poolcleanapp/ProviderTracking/getAppointmentDetails/${appointmentId}/`, {
            method: 'GET',
            headers: {'Content-Type': 'application/json'}
        });

        if (!appointmentResponse.ok) {
            throw new Error('Failed to fetch appointment details');
        }

        const appointmentDetails = await appointmentResponse.json();
        console.log('Appointment Details:', appointmentDetails);

        // Set the global company and client IDs
        globalCompanyId = appointmentDetails.c;
        globalClientId = appointmentDetails.cl;

        // Update the form fields with the fetched IDs
        document.getElementById('companyId').value = globalCompanyId;
        document.getElementById('clientId').value = globalClientId;

        // Fetch task data now that global IDs are set
        fetchTaskpingData();

        // Fetch more client details
        const clientResponse = await fetch(`/poolcleanapp/ProviderTracking/client/${globalClientId}/`, {
            method: 'GET',
            headers: {'Content-Type': 'application/json'}
        });

        if (!clientResponse.ok) {
            throw new Error('Failed to fetch client details');
        }

        const clientData = await clientResponse.json();
        console.log("Client Name is: " + clientData.fname + " " + clientData.lname);
        console.log("Client address is: " + clientData.address);

        // Update HTML elements with the client details
        document.getElementById('clientName').textContent = clientData.fname + ' ' + clientData.lname;
        document.getElementById('clientAddress').textContent = 'Address: ' + clientData.address;
        
    } catch (error) {
        console.error('Error:', error);
    }
}


function getCSRFToken() {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim().split('=');
        if (cookie[0] === 'csrftoken') {
            return decodeURIComponent(cookie[1]);
        }
    }
    return null;
}
 

document.getElementById('submitTasksButton').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    if (!globalCompanyId || !globalClientId) {
        console.log("No Company or Client ID");
        alert("No Company or Client ID set. Please select an appointment first.");
        return;  // Stop execution if IDs are not available
    }

    var taskNames = [];
    document.querySelectorAll('.form-check-input:checked').forEach(function(item) {
        taskNames.push(item.value);  // Collect all checked task names
    });

    if (taskNames.length === 0) {
        alert("Please select at least one task.");
        return;  // Prevent submission if no tasks are selected
    }

    var url = `/poolcleanapp/ProviderTracking/submit_task/${globalCompanyId}/${globalClientId}/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Ensure this function retrieves a valid token
        },
        body: JSON.stringify({
            tasknames: taskNames,
            status: 'n',
            description: 'Add a description'
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to submit tasks: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        alert("Tasks submitted successfully.");
        // Optionally, you can clear the checked items or refresh the task list
        document.querySelectorAll('.form-check-input:checked').forEach(item => item.checked = false);
        fetchTaskpingData();  // Refresh the task data if needed
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error submitting tasks: " + error.message);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    fetchTaskpingData(); // Ensure this is the right place to call it
    updateTask();
});

function fetchTaskpingData() {
    if (globalCompanyId === null || globalClientId === null) {
        console.error("Company ID or Client ID is not set.");
        return;
    }

    fetch(`/poolcleanapp/ProviderTracking/taskping/${globalCompanyId}/${globalClientId}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log("All data received:", data);
        const container = document.getElementById('taskpingContainer');
        container.innerHTML = '';  // Clear previous entries

        let allTasksCompleted = true;  // Flag to check if all tasks are completed

        data.forEach(task => {
            console.log("Task ID is: " + task.task_id);
            const taskElement = document.createElement('div');
            taskElement.className = 'task';
            const updatedDate = new Date(task.updated_at);
            const formattedTime = updatedDate.toLocaleString();

            let statusElement, descriptionElement, updateButton;
            if (task.status === 'y') {
                statusElement = `<div class="task-status-complete">Completed</div>`;
                descriptionElement = `<div class="task-description">${task.description}</div>`;
                updateButton = `<button id="button-container" disabled="disabled">Update</button>`;
            } else {
                allTasksCompleted = false;  // Mark flag as false if any task is incomplete
                statusElement = `
                    <select class="task-status" id="status-${task.task_id}">
                        <option value="y">Completed</option>
                        <option value="n" selected>In Progress</option>
                    </select>`;
                descriptionElement = `
                    <input type="text" class="task-description" id="description-${task.task_id}" value="${task.description || ''}">`;
                updateButton = `<button id="button-container" onclick="updateTask(${task.task_id})">Update</button>`;
            }

            taskElement.innerHTML = `
            <div class="task-title" style="font-weight: bold;">${task.taskname}</div>
            <div class="update-time" style="font-weight: bold;">Time of update: ${formattedTime}</div>
            ${statusElement}
            <div style="font-weight: bold;">Description:</div>
            ${descriptionElement}
            ${updateButton}
        `;
            container.appendChild(taskElement);
        });

        if (allTasksCompleted) {
            const completeButton = document.createElement('button');
            completeButton.textContent = 'Complete';
            completeButton.onclick = function() {
                if (confirm('Complete for the day?')) {
                    alert('Great job! Go back to Select an Appointment tab to select another appointment');
                } else {
                    alert('Continue your work!');
                }
            };
            container.appendChild(completeButton);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}




function updateTask(taskId) {

    if (!taskId) {
        console.error('Invalid Task ID provided.');
        return;
    }
    const status = document.getElementById(`status-${taskId}`).value;
    const description = document.getElementById(`description-${taskId}`).value;


    fetch(`/poolcleanapp/ProviderTracking/updateTask/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() 
        },
        body: JSON.stringify({
            status: status,
            description: description
        })
    })
    .then(response => response.ok ? response.json() : Promise.reject('Failed to update task'))
    .then(data => {
        console.log('Update Success:', data);
        fetchTaskpingData();  
    })
    .catch(error => {
        console.error('Error updating task:', error);
    });
}
