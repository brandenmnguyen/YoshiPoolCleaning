from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

# uses ChromeDriver with Chrome version = 123

# NOTE: To run only these functional tests use this command:
# python3 manage.py test poolcleanapp.tests.tests_functions

# NOTE: in order to test client and provider login,
# this assumes you already have a client with
# email = john.doe@example.com, password = password
# and assumes you already have provider
# email = pool.cleaner@example.com password, = password
# in the database

class ClientSignUpTests(LiveServerTestCase):

    def setUp(self):
        co = webdriver.ChromeOptions()
        co.browser_version = "123"
        self.driver = webdriver.Chrome(co)

    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def testGoToClientSignUp(self):
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

        assert 'Client SignUp page' in driver.title

    def testFillingInClientFields(self):
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
        register = driver.find_element(By.CLASS_NAME, 'signUpButton')
        
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


class ClientLoginTest(LiveServerTestCase):

    def setUp(self):
        co = webdriver.ChromeOptions()
        co.browser_version = "123"
        self.driver = webdriver.Chrome(co)

        self.clientEmail = 'john.doe@example.com'
        self.clientPassword = 'password'

    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def testGoToClientLogin(self):
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

        # manually enter otp code
        getpass.getpass("Press enter after entering otp.")

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
        

class ProviderSignUpTest(LiveServerTestCase):
    def setUp(self):
        co = webdriver.ChromeOptions()
        co.browser_version = "123"
        self.driver = webdriver.Chrome(co)

    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def testGoToProviderSignUp(self):
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

        # temp hide image that obscures sign up provider button
        img = driver.find_element(By.XPATH, "//img[@class='imagePoolSize']")
        driver.execute_script("arguments[0].style.visibility='hidden'", img)
        
        # find provider button and click
        provider_btn = driver.find_element(By.ID, "provider")
        provider_btn.click()

        # wait for page to load with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        assert 'Provider SignUp page' in driver.title

    def testFillingInProviderFields(self):
        driver = self.driver
        # start at signup page
        driver.get('http://127.0.0.1:8000/poolcleanapp/providersignup/')
        current_url = driver.current_url

        # get all fields

        name = driver.find_element(By.ID, 'companyName')
        address = driver.find_element(By.ID, 'companyAddress')
        phone_number = driver.find_element(By.ID, 'companyPhone')
        email = driver.find_element(By.ID, 'companyEmail')
        password = driver.find_element(By.ID, 'companyPassword')
        register = driver.find_element(By.CLASS_NAME, 'signUpButton')
        
        # create fake provider
        name.send_keys('Pool Cleaners Test 2')
        phone_number.send_keys(678912345)
        email.send_keys('pool.cleaner2@example.com')
        address.send_keys('2341 Gibson Road')
        password.send_keys('password')
        register.click()

        # wait until it goes back to login, with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        assert 'Login' in driver.title


class ProviderLoginTest(LiveServerTestCase):

    def setUp(self):
        co = webdriver.ChromeOptions()
        co.browser_version = "123"
        self.driver = webdriver.Chrome(co)

        self.providerEmail = 'pool.cleaner@example.com'
        self.providerPassword = 'password'

    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def testLoginProvider(self):
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
        email.send_keys(self.providerEmail)
        password.send_keys(self.providerPassword)

        # find login as provider button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a provider']")
        loginClientBtn.click()

        # wait for page to load with 10 second timeout
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))

        # manually enter otp code
        getpass.getpass("Press enter after entering otp.")

        assert 'ProviderTrackPage' in driver.title

    def testMissingEmailFieldProvider(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        # find password field and inject it
        password = driver.find_element(By.ID, 'password')
        password.send_keys(self.providerPassword)

        # find login as provider button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a provider']")
        loginClientBtn.click()

        # wait and see if warning pops up
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is missing']")))
        
    def testMissingPasswordFieldProvider(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        # find email field and inject it
        email = driver.find_element(By.ID, 'email')
        email.send_keys(self.providerEmail)

        # find login as provider button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a provider']")
        loginClientBtn.click()  

        # wait and see if warning pops
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is missing']")))
        
    def testIncorrectPasswordProvider(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        # find email and password
        email = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'password')
        # inject email and password, but use a wrong password
        email.send_keys(self.providerEmail)
        password.send_keys('WRONG_PASSWORD_TEST')

        # find login as provider button and click it
        loginClientBtn = driver.find_element(By.XPATH, "//button[text()='Login as a provider']")
        loginClientBtn.click()  

        # wait and see if warning pops
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is incorrect']")))
    

    def testProviderPressesClient(self):
        # start from login page
        driver = self.driver
        driver.get('http://127.0.0.1:8000/poolcleanapp/login/')

        current_url = driver.current_url
        # find email and password field
        email = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'password')

        # inject email and password field
        email.send_keys(self.providerEmail)
        password.send_keys(self.providerPassword)

        # find client login button and click it
        providerLoginBtn = driver.find_element(By.XPATH, "//button[text()='Login as a client']")
        providerLoginBtn.click()

        # wait and see if warning pops
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, 
                                                                             "//strong[text()='Email or password is incorrect']")))
