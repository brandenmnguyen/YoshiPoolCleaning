const ticketsData = [
  {
    amount: "$223.99",
    orderNumber: "Order No.: 987654",
    status: "Processed",
    clientName: "Alice Johnson",
    paymentMethod: "Credit Card",
    createdAt: new Date("2023-09-15T23:59:00"),
  },
  {
    amount: "$2237.00",
    orderNumber: "Order No.: 123456",
    status: "In Progress",
    clientName: "Bob Smith",
    paymentMethod: "PayPal",
    createdAt: new Date("2023-09-14T23:59:00"), // Add the current date and time
  },
  {
    amount: "$0.01",
    orderNumber: "Order No.: 192837",
    status: "Processed",
    clientName: "Charlie Davis",
    paymentMethod: "Debit Card",
    createdAt: new Date("2023-09-14T23:59:00"), // Add the current date and time
  },
  {
    amount: "$79.99",
    orderNumber: "Order No.: 564738",
    status: "In Progress",
    clientName: "Dana Lee",
    paymentMethod: "Bank Transfer",
    createdAt: new Date("2023-09-14T23:59:00"), // Add the current date and time
  },
  {
    amount: "$324.99",
    orderNumber: "Order No.: 56434738",
    status: "Processed",
    clientName: "David Miller",
    paymentMethod: "Check",
    createdAt: new Date("2023-09-16T23:59:00"), // Add the current date and time
  },
];

function updateTickets() {
  const ticketContainers = document.querySelectorAll(".payment-background");

  ticketContainers.forEach((container, index) => {
    if (index < ticketsData.length) {
      const clientNameElement = container.querySelector(".client-name");
      const paymentMethodElement = container.querySelector(".payment-method");
      const amountElement = container.querySelector(".task-money");
      const orderNumberElement = container.querySelector(".order-number");
      const dateTimeElement = container.querySelector(".date-time-position"); // Select the date-time element
      const transactionStatusElement = container.querySelector(".transaction");

      // Assuming all tickets now have a 'createdAt' property
      const ticket = ticketsData[index];

      if (clientNameElement) clientNameElement.textContent = ticket.clientName;
      if (paymentMethodElement)
        paymentMethodElement.textContent = ticket.paymentMethod;
      if (amountElement) amountElement.textContent = ticket.amount;
      if (orderNumberElement)
        orderNumberElement.textContent = ticket.orderNumber;
      if (dateTimeElement)
        dateTimeElement.textContent = formatDate(ticket.createdAt); // Format and set the date-time

      // Update the transaction status and class based on the ticket status
      if (transactionStatusElement) {
        transactionStatusElement.textContent =
          ticket.status === "Processed"
            ? "✔ Payment Processed"
            : "● Payment in Progress";
        transactionStatusElement.className = `transaction ${
          ticket.status === "Processed"
            ? "transaction-complete"
            : "transaction-in-progress"
        }`;
      }
    } else {
      container.style.display = "none"; // Hide containers without corresponding data
    }
  });
}

// Helper function to format the date
function formatDate(date) {
  // Format the date as 'M/D/YYYY h:mm:ss A' or any other format you prefer
  let hours = date.getHours();
  let minutes = date.getMinutes().toString().padStart(2, "0");
  let ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  let strTime =
    date.getMonth() +
    1 +
    "/" +
    date.getDate() +
    "/" +
    date.getFullYear() +
    " " +
    hours +
    ":" +
    minutes +
    " " +
    ampm;
  return strTime;
}

document.addEventListener("DOMContentLoaded", updateTickets);
