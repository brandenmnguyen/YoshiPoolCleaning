# Pool Clean Pro

<img src="https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/100047116/c6b18071-4068-4fa4-8741-8245bf304d37" width="256">

## Introduction

The pool cleaning industry, often underestimated, plays a crucial role for pool owners. Typically, interactions between pool technicians and clients are minimal, with clients only discovering the condition of their pools after maintenance is completed. Additionally, scheduling and payments can present challenges. To address these issues and revolutionize the industry, Ben Stewart, President of Stewart Industries, is seeking to develop a web application. This platform will enable clients to effortlessly find pool cleaning services, while also allowing pool cleaning companies to connect with potential clients.

This web application improves the way pool technicians and their companies operate. It lets technicians track and share their progress with clients, who no longer have to wonder when their pool will be cleaned. The app includes a straightforward scheduling system, making it easy for both technicians and clients to book appointments. Additionally, it features a payment system using Stripe, simplifying transactions and making the whole process smoother for everyone involved.

## Key Features

**Appointment Scheduling**

- A provider can add available appointment times for any customer to see.

- A customer can view those available times and schedule it with their provider, which will take them through the payment process.

- Once a customer schedules an appointment, the Provider can view it from their tracking page, add tasks, and update the info and status of those tasks.

- A customer can view their scheduled appointments and see what tasks were done and any notes that their pool service provider left them.

**Payment through the application:**

- Customers can use the application to pay the pool cleaners through different methods such as credit card or Paypal.

- The payment system uses the Stripe API.

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

## Application Screenshots

**Customer Side:**

- **Search For Pool Company**
  
![image](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/61b0c95d-4fe4-4458-93de-b12ee4f3f308)

- **Payment Page**

![image](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/7a0607e6-067e-4cc2-92a6-79849e899226)

- **Stripe Processing Payment**

![image](https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/114447703/ced8f637-d05f-4f7a-9ebd-83cff745984c)

**Pool Company Side:**

- **Select Appointment**
  
<img width="1097" alt="select appointment" src="https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/116032314/1dcb20ed-9431-4463-a57a-74f1edb22458">
  
- **Selecting Task**

<img width="1082" alt="add task" src="https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/116032314/0d4d3870-85b9-4865-8737-79d5bdf141f1">
  
- **Update Task**
  
<img width="407" alt="update task" src="https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/116032314/2d1c89e9-a0dd-4ede-bd00-87314c2aa9a7">
  
- **Complete Task**

<img width="1075" alt="task description" src="https://github.com/brandenmnguyen/YoshiPoolCleaning/assets/116032314/9c10b570-e128-43ce-8035-1cb94d3d9a4f">

## Testing

This project uses Django's built-in testing tools for unit testing and Selenium for functional testing. To ensure your development environment is ready for running tests, you will need to install the necessary dependencies and configure your system appropriately.

### Prequisites:

- **Python:** Make sure you have Python installed. You can download it from [python.org](https://www.python.org/)
- **ChromeDriver:** Make sure you have ChromeDriver installed. You can download it from [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

### Activate and Run Python Virtual Environment

1. Create a python virtual environment
```
python3 -m venv venv
```
2. Activate virtual environment
```
source venv/bin/activate
```
3. Install all python dependencies
```
pip install -r requirements.txt
```

### Run Tests

- You can run all the tests with this command
```
python3 manage.py test
```
- To run a specific test, run python3 manage.py test poolcleanapp.tests.<FILE_NAME>
  For example, to test only models, run the following command:
```
python3 manage.py test poolcleanapp.tests.tests_models
```
- To run only functional tests, first start the server
```
python3 manage.py runserver
```
  Then on a separate window, run this command
```
python3 manage.py test poolcleanapp.tests.tests_functions
```
  
## Deployment

* We used Amazon Web Services to host the web application. The deployed web application can be viewed at [https://poolcleanpro.net/poolcleanapp/homepage/](https://poolcleanpro.net/poolcleanapp/homepage/).
* You can learn about how to deploy with the [AWS deployment documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

## Developer Instructions

To set up the development environment for this project: 
- First, ensure that you have Visual Studio Code and Python installed on your computer.
- After, start by cloning the project repository using the command git clone using the URL of Project, then navigate into the project directory. 
- Create a virtual environment within the project directory by running python -m venv venv, and activate it using .\\venv\\Scripts\\activate on Windows or source venv/bin/activate on MacOS/Linux. 
- Install all required dependencies. 
- Finally, open the project in Visual Studio Code by running code in the terminal within your project directory.

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

### APIs

- **Geolocation API:** To Track User Location
  - **Cost:** Free

- **Google Maps Embed API:** embeds google maps into pages
  - **Cost:** Free

- **Stripe API:** To Process Payments
  - **Cost:** 2.9% + 30 cents per card charge

### Version Control

- [GitHub](https://github.com/): A web-based platform for version control and collaboration.

### Deployment

- [AWS](https://aws.amazon.com): Which stands for Amazon Web Services, allows deploying applications and services with greater flexibility, scalability, and reliability.

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
