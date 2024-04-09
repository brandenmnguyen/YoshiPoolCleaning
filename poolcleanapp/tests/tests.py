'''
from django.test import SimpleTestCase, TestCase
from django.test import Client as TestClient
from django.urls import reverse, resolve
from poolcleanapp.models import Client
from poolcleanapp.views import homepage
from poolcleanapp.views import about
from poolcleanapp.views import providertracking
from poolcleanapp.views import clienttracking
from ..models import Client, Company

import json

# Create your tests here.from django.test import TestCase

class TestUrls(SimpleTestCase):
    def test_homepage(self):
        self.client = TestClient()  # Create a client object for making requests
        url = reverse('homepage/')
        response = self.client.get(url)  # Perform a GET request to the URL
        print(resolve(url))
        self.assertTemplateUsed(response, 'Homepage-1.html')  # Check if the correct template is used
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200

class TestUrlsAbout(SimpleTestCase):
    def test_homepage(self):
        client = TestClient()  # Create a client object for making requests
        url = reverse('about')
        response = client.get(url)  # Perform a GET request to the URL
        print(resolve(url))
        self.assertTemplateUsed(response, 'about.html')  # Check if the correct template is used
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200

class TestUrlsTracking(SimpleTestCase):
    def test_homepage(self):
        client = TestClient()  # Create a client object for making requests
        url = reverse('providertracking')
        response = client.get(url)  # Perform a GET request to the URL
        print(resolve(url))
        self.assertTemplateUsed(response, 'ProviderTracking.html')  # Check if the correct template is used
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200

class TestUrlsTrackingClient(SimpleTestCase):
    def test_homepage(self):
        client = TestClient()  # Create a client object for making requests
        url = reverse('clienttracking')
        response = client.get(url)  # Perform a GET request to the URL
        print(resolve(url))
        self.assertTemplateUsed(response, 'ClientTracking.html')  # Check if the correct template is used
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
'''