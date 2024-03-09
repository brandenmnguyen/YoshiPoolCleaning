from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# NOTE: To run only these functional tests use this command:
# python3 manage.py test poolcleanapp.functional_tests

class ClientSignUpTests(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def testGoToSignUp(self):
        driver = self.driver
        # start at homepage
        driver.get('http://127.0.0.1:8000/poolcleanapp/homepage/')
        current_url = driver.current_url

        # find login button and click
        login_btn = driver.find_element(By.CLASS_NAME, 'rightButton')
        login_btn.click()

        # wait for page to load with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        current_url = driver.current_url

        # find sign up button and click
        signup_btn = driver.find_element(By.ID, 'provider')
        signup_btn.click()

        # wait for page to load with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        assert 'Client Registration' in driver.title

    def testFillingInFields(self):
        driver = self.driver
        # start at signup page
        driver.get('http://127.0.0.1:8000/poolcleanapp/clientsignup/')
        current_url = driver.current_url

        # get all fields

        # check if first name field exists
        first_name = driver.find_element(By.ID, 'clientfname')
        last_name = driver.find_element(By.ID, 'clientlname')
        phone_number = driver.find_element(By.ID, 'clientphonenumber')
        email = driver.find_element(By.ID, 'clientemail')
        address = driver.find_element(By.ID, 'clientaddress')
        password = driver.find_element(By.ID, 'client_password')
        register = driver.find_element(By.TAG_NAME, 'button')
        
        first_name.send_keys('John')
        last_name.send_keys('Doe')
        phone_number.send_keys(987654321)
        email.send_keys('john.doe@example.com')
        address.send_keys('123 Main Street')
        password.send_keys('password')
        register.click()

        # wait until it goes back to login, with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        assert 'Login' in driver.title


class ClientProviderLoginTest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.clientEmail = 'john.doe@example.com'
        self.clientPassword = 'password'

    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def testGoToLogin(self):
        # start from homepage
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/homepage/')
        current_url = driver.current_url

        # find login button and check if it's displayed
        login_btn = driver.find_element(By.CLASS_NAME, 'rightButton')
        assert login_btn.is_displayed

        # click on the button and go to next page with 10 second timeout
        login_btn.click()
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        assert 'Login' in driver.title

    def testLoginClient(self):
        # NOTE: NEED TO HAVE AN ACCOUNT WITH EMAIL: john.doe@example.com
        # AND PASSWORD: password FOR THIS TEST TO WORK

        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')
        current_url = self.driver.current_url
        # find email field
        email = driver.find_element(By.ID, 'email')

        # find password field
        password = driver.find_element(By.ID, 'password')

        # inject fields with an already created account
        email.send_keys(self.clientEmail)
        password.send_keys(self.clientPassword)

        # find login as client button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a client']")
        loginClientBtn.click()

        # wait for page to load with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        assert 'ClientTrackPage' in driver.title

    def testMissingEmailFieldClient(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        # find password field and inject it
        password = driver.find_element(By.ID, 'password')
        password.send_keys(self.clientPassword)

        # find login as client button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a client']")
        loginClientBtn.click()

        # wait and see if warning pops up
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is missing']")))
        
    def testMissingPasswordFieldClient(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        # find email field and inject it
        email = driver.find_element(By.ID, 'email')
        email.send_keys(self.clientEmail)

        # find login as client button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a client']")
        loginClientBtn.click()  

        # wait and see if warning pops
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is missing']")))
        
    def testIncorrectPasswordClient(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        # find email and password
        email = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'password')
        # inject email and password, but use a wrong password
        email.send_keys(self.clientEmail)
        password.send_keys('WRONG_PASSWORD_TEST')

        # find login as client button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a client']")
        loginClientBtn.click()  

        # wait and see if warning pops
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is incorrect']")))
    

    def testClientPressesProvider(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        current_url = driver.current_url
        # find email and password field
        email = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'password')

        # inject email and password field
        email.send_keys(self.clientEmail)
        password.send_keys(self.clientPassword)

        # find provider login button and click it
        providerLoginBtn = driver.find_element(By.XPATH, "//button[text()='Login as a provider']")
        providerLoginBtn.click()

        # wait and see if warning pops
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is incorrect']")))