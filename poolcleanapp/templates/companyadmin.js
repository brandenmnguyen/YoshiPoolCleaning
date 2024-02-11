let employeeCount = 0;
let addedEmployees = [];

function addEmployee() {
    const employeeName = document.getElementById('employeeName').value;
    const employeeEmail = document.getElementById('employeeEmail').value;
    const employeeID = document.getElementById('employeeID').value;
    const employeeRole = document.getElementById('employeeRole').value;
    const companyName = document.getElementById('companyName').value;

    const formNotice = document.getElementById('formNotice');


    // Email validation using regular expression
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const isValidEmail = emailPattern.test(employeeEmail);



    if (employeeName && isValidEmail && employeeID && employeeRole && companyName) {
        // Check for duplicates
        const isDuplicate = addedEmployees.some(emp => emp.employeeID === employeeID);

        if (!isDuplicate) {
            employeeCount++;

            const newCard = document.createElement('div');
            newCard.classList.add('card', 'col-md-6', 'mb-4');
            
            // Set data-employee-id attribute
            newCard.setAttribute('data-employee-id', employeeID);
            newCard.innerHTML = `
            <div class="card-body">
                <button class="btn btn-warning btn-sm float-right ml-1" onclick="editEmployee('${employeeID}')">Edit</button>
                <button class="btn btn-danger btn-sm float-right" onclick="deleteEmployee('${employeeID}')">X</button>
                <h5 class="card-title">${employeeName}</h5>
                <p class="card-text">Email: ${employeeEmail}</p>
                <p class="card-text">ID: ${employeeID}</p>
                <p class="card-text">Role: ${employeeRole}</p>
                <p class="card-text">Company: ${companyName}</p>
            </div>
        `;
        

            document.getElementById('employeeDeck').appendChild(newCard);
            formNotice.textContent = ''; // Clear the notice

            // Add employee to the list of added employees
            addedEmployees.push({
                employeeID: employeeID,
                employeeName: employeeName,
                employeeEmail: employeeEmail,
                employeeRole: employeeRole,
                companyName: companyName
            });

        } else {
            formNotice.textContent = 'Employee with the same ID already exists. Please use a different ID.';
        }
    } else {
        formNotice.textContent = 'Please fill out all fields correctly before adding an employee.';
    }



    // Create a delete button
    const deleteButton = document.createElement('button');
    deleteButton.classList.add('btn', 'btn-danger', 'btn-sm', 'float-right');
    deleteButton.innerHTML = 'X';
    // Add a click event to delete the employee
    deleteButton.addEventListener('click', function () {
        const confirmation = confirm('Are you sure you want to delete this employee?');
        if (confirmation) {
            // Delete the card when confirmed
            newCard.remove();
            removeFromAddedEmployees(employeeID); // Remove from addedEmployees array
            updateNavigationVisibility();
        }
    });

// Append the delete button to the card
newCard.querySelector('.card-body').appendChild(deleteButton);

// Set data-employee-id attribute
newCard.setAttribute('data-employee-id', employeeID);
}

function removeFromAddedEmployees(employeeID) {
    addedEmployees = addedEmployees.filter(emp => emp.employeeID !== employeeID);
}

function deleteEmployee(employeeID) {
    const confirmation = confirm('Are you sure you want to delete this employee?');
    if (confirmation) {
        const cardToDelete = document.querySelector(`.card[data-employee-id="${employeeID}"]`);
        cardToDelete.remove();
        removeFromAddedEmployees(employeeID);
        updateNavigationVisibility();
    }
}

function editEmployee(employeeID) {
    const employeeToEdit = addedEmployees.find(emp => emp.employeeID === employeeID);

    // Fill modal fields with existing data
    document.getElementById('editEmployeeName').value = employeeToEdit.employeeName;
    document.getElementById('editEmployeeEmail').value = employeeToEdit.employeeEmail;
    document.getElementById('editEmployeeID').value = employeeToEdit.employeeID;
    document.getElementById('editEmployeeRole').value = employeeToEdit.employeeRole;
    document.getElementById('editCompanyName').value = employeeToEdit.companyName;

    // Find the card using data-employee-id
    const cardToEdit = document.querySelector(`.card[data-employee-id="${employeeID}"]`);

    // Open the modal
    $('#editEmployeeModal').modal('show');
}


function saveEmployeeChanges() {
    const employeeID = document.getElementById('editEmployeeID').value;

    // Find the employee in the addedEmployees array
    const index = addedEmployees.findIndex(emp => emp.employeeID === employeeID);

    // Update employee information with edited values
    addedEmployees[index].employeeName = document.getElementById('editEmployeeName').value;
    addedEmployees[index].employeeEmail = document.getElementById('editEmployeeEmail').value;
    addedEmployees[index].employeeRole = document.getElementById('editEmployeeRole').value;
    addedEmployees[index].companyName = document.getElementById('editCompanyName').value;

    // Find the card in the employeeDeck
    const cardToUpdate = document.querySelector(`[data-employee-id="${employeeID}"]`);
    cardToUpdate.querySelector('.card-title').textContent = addedEmployees[index].employeeName;
    cardToUpdate.querySelector('.card-text:nth-child(2)').textContent = `Email: ${addedEmployees[index].employeeEmail}`;
    cardToUpdate.querySelector('.card-text:nth-child(3)').textContent = `ID: ${addedEmployees[index].employeeID}`;
    cardToUpdate.querySelector('.card-text:nth-child(4)').textContent = `Role: ${addedEmployees[index].employeeRole}`;
    cardToUpdate.querySelector('.card-text:nth-child(5)').textContent = `Company: ${addedEmployees[index].companyName}`;

    // Hide the edit modal
    $('#editEmployeeModal').modal('hide');
}