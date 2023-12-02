# Yoshi Pool Cleaning

![templogo](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/db209675-7c78-479c-a352-f8425947c8cd)

## Introduction

The pool cleaning industry is one that is quite overlooked, but important for those who own pools. Wanting to create a big splash in the industry, our client, Ben Stewart, President of Stewart Industries, wants us to create a web application for clients to find pool cleaners, and for pool cleaning companies to be able to find customers with pools to clean.

## Key Features

**Location tracking:** 

- The application can track when a pool cleaner checks in and checks out in regards to cleaning the pool

- The application uses time stamps to indicate when the pool cleaner has signed in and signed out.

**Payment through the application:**

- Customers can use the application to pay the pool cleaners through different methods such as credit card or Paypal.

- The payment system uses the Stripe API.

**Real time communication:**

- Customers can directly message the pool cleaner and the pool cleaner can directly message the customer.

- The communication will be in real time.

**Login System**

- Customers can sign up and create an account

- Pool companies can create company accounts and assign employees accounts associated with the company

**Search system:**

- Customers can search up and select the pool company that they would like to select

- Pool cleaning companies can list themselves and search for customers that need assistance.

**Calendar:**

- Both customers and pool cleaning companies can utilize a calendar to see their booked pool cleaning appointments.

## Prototype Images

- **Entity Relationship Diagram**

![er](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/6c0763fe-c86a-4b54-8c34-201818fbf42a)

- **Project Mockup in Figma**

![mockup](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/ee468009-5fb9-4ab4-bc4f-77d974fdaf6f)

- **Payment Page**

![sampleimage1](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/465ba3cf-0c48-4923-b36b-1bd161883f72)

- **Client Tracking Page**

![sampleimage2](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/0f3c71c6-7baf-4464-80c7-d6c57c7effc2)

- **Login Page**

![sampleimage3](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/b28d9c69-1666-4acb-956e-ebcde57ca105)

## Testing

To be added in CSC191

## Deployment

To be added in CSC191

## Developer Instructions

To be added in CSC191

## Tech Stack

This project is built using the following technologies and tools:

### Frontend

**Programming Languages:** HTML, CSS, JavaScript, JSON
  
- **Interactive Development Environment (IDE):**
  
  [Visual Studio Code](https://code.visualstudio.com/): A lightweight but powerful source code editor.

- **Front-end Framework:**
  
  [Bootstrap](https://getbootstrap.com/): A popular HTML, CSS, and JavaScript framework for building responsive and mobile-first web pages.

### Backend

- **Programming Languages:** SQL, Python, C, JSON

- **Relational Database:**
  
  [MySQL](https://www.mysql.com/): An open-source relational database management system.

- **Web Framework:**
  
  [Django](https://www.djangoproject.com/): A high-level Python web framework that encourages rapid development and clean, pragmatic design.

- **Authentication Library:**
  
  [django-otp](https://django-otp-official.readthedocs.io/): Django library for two-factor authentication.

- **Web Server:**
  
  [Apache](https://httpd.apache.org/): A widely used open-source web server.

### APIs

- **Geolocation API:** To Track User Location
  - **Cost:** Free

- **Google Maps Embed API:** embeds google maps into pages
  - **Cost:** Free

- **Stripe API:** To Process Payments
  - **Cost:** 2.9% + 30 cents per card charge

### Version Control

- [GitHub](https://github.com/): A web-based platform for version control and collaboration.

### Servers

- [Microsoft Azure](https://azure.microsoft.com/): A cloud computing service for building, testing, deploying, and managing applications and services.

## Timeline

### Sprint 5
- Finish Login and Sign up for Clients
- Finish Login and Sign up for Providers
- Make Custom 404 page for invalid url(s)
- Work on invoice tracking page so it works with fake data
- Automatically Populate provider search based on the database
- Create company admin page
- Let company admins create and delete employee accounts
- Work on back-end logic for client scheduling appointment for service

### Sprint 6
- Populate invoice tracking page using the database
- Work on back-end logic for provider to view daily tasks
- Work on provider daily calendar to view daily tasks using fake data
- Work on back-end logic to return tasks to either provider or client
- Work on client tracking page so that it works with fake data
- Work on provider tracking page so that it works with fake data
- Work on back-end logic of client subscribing to a provider
- Work on front-end allowing client to subscribe to a provider
- Finalize layout of payment page and allow it to capture user information
- Make initial back-end logic for processing payments without Stripe API 

### Sprint 7
- Work on and apply Stripe API integration into the back-end
- Add one-time card payments using Stripe API
- Have payment page submit payments and save those payments in the database
- Populate client tracking page based on database
- Populate provider tracking page based on database
- Work on back-end logic for verifying if provider is at a client's location using the HTML Geolocation API
- Get two factor authentication working for both clients and providers
- Let provider mark certain tasks as done for the client to see
- Have local database update to the cloud instead

### Sprint 8
- Get webapp uploaded and deployed on Microsoft Azure
- Allow providers to mark tasks as incomplete if they run into issues as they are completing them for the client
- Get push notifications working for provider arriving at a client's house
- Implement feature for clients to unsubscribe from a provider
- Implement prototype for chatting between client and provider
- basic implementation of client dashboard that shows which provider the client is subscribed to
- Implement website fees 

### Sprint 9
- Fix any outstanding bugs
- Implement client being able to reschedule provider services
- Implement providers setting client Sign up limit 
- Tweak search algorithm for provider search page to sort by closest providers to client's home
- Implement password changing options for both the client and the provider
- Add password length and format requirements for security reasons
- Implement recurring payments for the clients
- Allow providers to remove clients

## Contact

Please contact Yoshi via Sac State email for any inquiries.

- Arin Sparrow (Development Team) aringsparrow@csus.edu
- Davidson Au (Development Team) davidsonau@csus.edu
- Samantha Ceralde (Development Team) samanthaceralde@csus.edu
- Branden Nguyen (Development Team) brandenmnguyen@csus.edu
- Mohammed Al Chalabi (Development Team) mohammedalchalabi@csus.edu
- Christopher Chafin (Development Team) cchafin@csus.edu
- Shahad Jaber (Development Team) sjaber@csus.edu
- William Flotte (Development Team) wflotte@csus.edu
- Eva Vashisth (Development Team) pprachi@csus.edu
