function updateLiveDate() {
  const dateElement = document.getElementById("liveDate");
  const now = new Date();
  const options = { weekday: "long", month: "long", day: "numeric" };
  dateElement.textContent = now.toLocaleDateString("en-US", options);
}

// Call the function to update the date when the script loads
updateLiveDate();
