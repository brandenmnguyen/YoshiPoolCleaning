//create array

const companyInformation = [
    { name: "Liquad FX", location: "4712 Sacramento, CA", phoneNumber: "(925)4930-394" },
    { name: "PoolGuysLLC", location: "8694 Rocklin, CA", phoneNumber: "(925)3895-953" },
    { name: "Poseidon Pool Service", location: "1983, Brentwood, CA", phoneNumber: "(916)9400-824" },
    { name: "NorCal Pools", location: "2351 Sunset bLVD, Rocklin, CA", phoneNumber: "(916)886-3828" },
    { name: "Matthews Pool Services", location: "877, Greater Sacramento Area, CA", phoneNumber: "(916)612-8877" },
    { name: "Above & Beyond Pool Service", location: "622 Farrington Ln, Lincolin, CA", phoneNumber: "(702)339-3878" }
];

const bodyofbody = document.querySelector(".contentOfConent"); //this is for the main body
const resultNumber = document.querySelector("#numberResults"); //this is for h2 element
const plusSigns = document.querySelector(".plusItself"); //this is for the div for the plus sign 

//get the length of the items in the array
resultNumber.textContent = `Showing ${companyInformation.length} results`;

//iterate through the whole array
companyInformation.forEach(company => {

    //creating elements 
    const mainContainer = document.createElement("div");
    const companyContainer = document.createElement("div");
    const secondContainer = document.createElement("div");
    const plus = document.createElement("a");

    plus.textContent = "+";

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

    //for css purposes
    mainContainer.classList.add("resultsOfSearch");
    companyContainer.classList.add("infoOfCompany");
    secondContainer.classList.add("plusSign");
    plus.classList.add("plusItself");

    
    secondContainer.appendChild(plus);

    mainContainer.appendChild(companyContainer);
    mainContainer.appendChild(secondContainer);
    
    bodyofbody.appendChild(mainContainer);
    bodyofbody.appendChild(line);

});