// Helper function to get the CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

console.log("Script loaded");

document.addEventListener("DOMContentLoaded", function () {
  // Attach event listeners to open modal buttons
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", function () {
      var action = this.getAttribute("data-action");
      switch (action) {
        case "email":
          openModal("changeEmailModal");
          break;
        case "password":
          openModal("changePasswordModal");
          break;
        case "address":
          openModal("changeAddressModal");
          break;
        case "phone":
          openModal("changePhoneModal");
          break;
        default:
          console.log("No action found");
      }
    });
  });

  // Attach event listeners to save change buttons inside modals
  document
    .getElementById("saveEmailChange")
    .addEventListener("click", submitEmailChange);
  document
    .getElementById("savePasswordChange")
    .addEventListener("click", submitPasswordChange);
  document
    .getElementById("saveAddressChange")
    .addEventListener("click", submitAddressChange);
  document
    .getElementById("savePhoneChange")
    .addEventListener("click", submitPhoneChange);
});

function openModal(modalId) {
  $(`#${modalId}`).modal("show");
}

function submitEmailChange() {
  const newEmail = document.getElementById("emailInput").value;
  updateClientDetails(clientId, { email: newEmail });
}

function submitPasswordChange() {
  const newPassword = document.getElementById("passwordInput").value;
  updateClientDetails(clientId, { password: newPassword });
}

function submitAddressChange() {
  const newAddress = document.getElementById("newAddressInput").value;
  updateClientDetails(clientId, { address: newAddress });
}

function submitPhoneChange() {
  const newPhone = document.getElementById("phoneInput").value;
  updateClientDetails(clientId, { phone_number: newPhone });
}

function confirmDeleteAccount() {
  // Call to a function that handles account deletion
  deleteClientAccount(clientId);
}

async function updateClientDetails(clientId, data) {
  try {
    // Construct the correct endpoint URL
    const endpoint = `/poolcleanapp/editaccount/update/${clientId}/`;

    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"), // Ensuring CSRF token is included
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Failed to update client details.");
    }

    const result = await response.json();

    if (result.success) {
      alert("Client details updated successfully!");
      location.reload(); // Optionally reload the page to reflect changes
    } else {
      throw new Error(result.message);
    }
  } catch (error) {
    console.error("Update failed:", error);
    alert("Failed to update client details: " + error.message);
  }
}

function deleteClientAccount(clientId) {
  if (
    confirm(
      "Are you sure you want to delete your account? This action cannot be undone."
    )
  ) {
    // Call to a function that handles account deletion
    console.log("Account deletion not implemented.");
  }
}
