//create array

const companyInformation = [

];

const bodyofbody = document.querySelector(".contentOfConent"); //this is for the main body
const resultNumber = document.querySelector("#numberResults"); //this is for h2 element
const plusSigns = document.querySelector(".plusItself"); //this is for the div for the plus sign 

//get the length of the items in the array
resultNumber.textContent = `Showing ${companyInformation.length} results`;

//iterate through the whole array
companyInformation.forEach(company => {

    // Creating elements 
    const mainContainer = document.createElement("div");
    const companyContainer = document.createElement("div");
    const secondContainer = document.createElement("div");
    const subscribeButton = document.createElement("button");

    subscribeButton.textContent = "Subscribe";

    const nameOfCompany = document.createElement("p");
    nameOfCompany.textContent = company.name;

    const locationOfCompany = document.createElement("p");
    locationOfCompany.textContent = company.location;

    const numberOfCompany = document.createElement("p");
    numberOfCompany.textContent = company.phoneNumber;

    const line = document.createElement("hr");

    nameOfCompany.classList.add("nameOfCompany");
    locationOfCompany.classList.add("nameOfStreet");
    numberOfCompany.classList.add("Phonenumber");

    companyContainer.appendChild(nameOfCompany);
    companyContainer.appendChild(locationOfCompany);
    companyContainer.appendChild(numberOfCompany);

    // For CSS purposes
    mainContainer.classList.add("resultsOfSearch");
    companyContainer.classList.add("infoOfCompany");
    secondContainer.classList.add("subscribeButton");

    subscribeButton.classList.add("subscribeItself");

    secondContainer.appendChild(subscribeButton);

    mainContainer.appendChild(companyContainer);
    mainContainer.appendChild(secondContainer);

    bodyofbody.appendChild(mainContainer);
    bodyofbody.appendChild(line);

});

// Add event listeners for subscription
const subscribeButtons = document.querySelectorAll(".subscribeItself");

subscribeButtons.forEach(button => {
    button.addEventListener("click", () => {
        button.classList.toggle("subscribed");
        button.textContent = button.classList.contains("subscribed") ? "Subscribed ✔" : "Subscribe";
    });
});