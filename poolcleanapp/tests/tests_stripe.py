from django.test import *
from django.urls import reverse, resolve
from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from poolcleanapp.views import *

class TestStripe(TestCase): 
    
    def setUp(self):
        chrome_driver_path = 'C:\\Users\\ibran\\Desktop\\drivers\\chromedriver.exe'
        co = webdriver.ChromeOptions()
        co.browser_version = "123"
        co.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
        self.driver = webdriver.Chrome(options=co)
        self.factory = RequestFactory()


    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def test_stripeTest(self):
        client = Client()
        response = client.get(reverse('stripe_test'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripeTest.html')

    def test_checkout(self, mock_stripe):
        request = self.factory.get(reverse('checkout'))
        response = checkout(request)
        self.assertEqual(response.status_code, 303)  

    def test_checkout2(self, mock_stripe):
        request = self.factory.get(reverse('checkout2'))
        response = checkout(request)
        self.assertEqual(response.status_code, 303) 

    def test_checkout3(self, mock_stripe):
        request = self.factory.get(reverse('checkout3'))
        response = checkout(request)
        self.assertEqual(response.status_code, 303) 

    def test_payment_history(self, mock_datetime, mock_stripe):
        mock_datetime.datetime.utcnow.return_value = datetime.datetime(2024, 4, 14, 12, 0, 0)
        request = self.factory.get(reverse('payment_history'))
        response = payment_history(request)
        self.assertEqual(response.status_code, 200)  
