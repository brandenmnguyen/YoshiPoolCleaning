const ticketsData = [
  {
    amount: "$44323.99",
    orderNumber: "Order No.: 4654",
    status: "In Progress",
    clientName: "Jessica Wilson",
    paymentMethod: "Credit Card",
    createdAt: new Date("2020-09-15T18:30:00"),
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
];

function updateTickets() {
  const container = document.querySelector(".payment-history-container"); // Select the container

  ticketsData.forEach((ticket) => {
    // Create the outermost 'row' and 'mt-3' div
    const rowDiv = document.createElement("div");
    rowDiv.classList.add("row", "mt-3");

    // Create the 'payment-background' div
    const paymentDiv = document.createElement("div");
    paymentDiv.classList.add(
      "payment-background",
      "d-flex",
      "flex-column",
      "justify-content-between"
    );

    // Create the inner structure with 'client-name', 'payment-method', etc.
    const contentDiv = document.createElement("div");
    contentDiv.classList.add("d-flex", "justify-content-between");

    // Client name and payment method section
    const taskTitleDiv = document.createElement("div");
    taskTitleDiv.classList.add("task-title", "d-flex", "align-items-center");
    const clientNameSpan = document.createElement("span");
    clientNameSpan.classList.add("client-name");
    clientNameSpan.textContent = ticket.clientName;
    const paymentMethodSpan = document.createElement("span");
    paymentMethodSpan.classList.add("payment-method");
    paymentMethodSpan.textContent = ticket.paymentMethod;

    taskTitleDiv.appendChild(clientNameSpan);
    taskTitleDiv.appendChild(document.createElement("br"));
    taskTitleDiv.appendChild(paymentMethodSpan);

    // Money and order number section
    const moneyOrderDiv = document.createElement("div");
    const taskMoneyDiv = document.createElement("div");
    taskMoneyDiv.classList.add("task-money");
    taskMoneyDiv.textContent = ticket.amount;
    const orderNumberDiv = document.createElement("div");
    orderNumberDiv.classList.add("order-number");
    orderNumberDiv.textContent = ticket.orderNumber;

    moneyOrderDiv.appendChild(taskMoneyDiv);
    moneyOrderDiv.appendChild(orderNumberDiv);

    // Date-time position
    const dateTimeDiv = document.createElement("div");
    dateTimeDiv.classList.add("date-time-position");
    dateTimeDiv.textContent = formatDate(ticket.createdAt);

    // Transaction status container
    const transactionContainerDiv = document.createElement("div");
    transactionContainerDiv.classList.add("d-flex", "justify-content-end");

    // Transaction status
    const transactionDiv = document.createElement("div");
    transactionDiv.classList.add(
      "transaction",
      ticket.status === "Processed"
        ? "transaction-complete"
        : "transaction-in-progress"
    );
    transactionDiv.textContent =
      ticket.status === "Processed"
        ? "✔ Payment Processed"
        : "● Payment in Progress";

    // Append the transaction status to its container
    transactionContainerDiv.appendChild(transactionDiv);

    // Assembling the structure
    contentDiv.appendChild(taskTitleDiv);
    contentDiv.appendChild(moneyOrderDiv);

    paymentDiv.appendChild(contentDiv);
    paymentDiv.appendChild(dateTimeDiv);
    paymentDiv.appendChild(transactionContainerDiv); // Append the transaction status container at the bottom

    rowDiv.appendChild(paymentDiv);

    // Append the assembled row to the container
    container.appendChild(rowDiv);
  });
}

// Keep the formatDate function as is

// Assuming formatDate function is defined elsewhere as provided previously

document.addEventListener("DOMContentLoaded", updateTickets);

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
