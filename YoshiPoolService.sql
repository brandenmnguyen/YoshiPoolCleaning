USE POOL;

CREATE TABLE EMPLOYEE (
    Employee_id INT PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    c_id INT,
    emp_password VARCHAR(255), 
    phone_number VARCHAR(15),
    is_owner ENUM('Y', 'N') DEFAULT 'N',  -- New column to indicate whether the employee is an owner, default is 'N'
    FOREIGN KEY (c_id) REFERENCES COMPANY (C_id)
);

CREATE TABLE COMPANY (
    C_id INT PRIMARY KEY,
    Company_Name VARCHAR(100),
    Company_Address VARCHAR(255),
    Company_Phone VARCHAR(15),
    Company_Email VARCHAR(100),
    Company_PW VARCHAR(255),
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES EMPLOYEE (Employee_id)
);

CREATE TABLE CLIENT (
    Client_id INT PRIMARY KEY,
    fname VARCHAR(100),
    lname VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    cl_password VARCHAR(255),
    phone_number VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE INVOICE (
    invoice_id INT PRIMARY KEY,
    client_id INT,
    emp_id INT,
    payment_date DATE,
    received_date DATE,
    amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    card_name VARCHAR(100),
    ExpDate DATE,
    email VARCHAR(100),
    reference_number VARCHAR(50),
    status VARCHAR(20),
    FOREIGN KEY (client_id) REFERENCES CLIENT (Client_id),
    FOREIGN KEY (emp_id) REFERENCES EMPLOYEE (Employee_id)
);

CREATE TABLE TASKPING (
    task_id INT PRIMARY KEY,
    status CHAR(1),
    taskName VARCHAR(100),
    description TEXT,
    emp_id INT,
    client_id INT,
    FOREIGN KEY (emp_id) REFERENCES EMPLOYEE (Employee_id),
    FOREIGN KEY (client_id) REFERENCES CLIENT (Client_id)
);

CREATE TABLE APPOINTMENTS (
    appointment_id INT PRIMARY KEY,
    cl_id INT,
    emp_id INT,
    appdate DATE,
    apptime TIME,
    FOREIGN KEY (cl_id) REFERENCES CLIENT (Client_id),
    FOREIGN KEY (emp_id) REFERENCES EMPLOYEE (Employee_id)
);