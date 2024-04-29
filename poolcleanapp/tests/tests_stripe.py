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
        co = webdriver.ChromeOptions()
        co.browser_version = "123"
        self.driver = webdriver.Chrome(co)
        self.factory = RequestFactory()


    def tearDown(self):
        # Clear cookies after each test
        self.driver.delete_all_cookies()
        self.driver.quit()

    def test_paymentpage(self):
        url = reverse('paymentpage')
        self.assertEqual(resolve(url).func, paymentPage)

    def test_checkout(self):
        request = self.factory.get(reverse('checkout'))
        response = checkout(request)
        self.assertEqual(response.status_code, 302) 

    def test_checkout2(self):
        request = self.factory.get(reverse('checkout2'))
        response = checkout(request)
        self.assertEqual(response.status_code, 302) 

    def test_checkout3(self):
        request = self.factory.get(reverse('checkout3'))
        response = checkout(request)
        self.assertEqual(response.status_code, 302) 

