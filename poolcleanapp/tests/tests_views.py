from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse, resolve

from poolcleanapp.models import Client, Company

class TestViews(TestCase):

    def setUp(self):
        self.client = TestClient()
        self.login_url = reverse("login")
        self.homepage_url = reverse('homepage')
        self.about_url = reverse('about')
        self.client_tracking_url = reverse('clienttracking')
        self.provider_tracking_url = reverse('providertracking')

    def test_homepage_GET(self):
        response = self.client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Homepage-1.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_client_tracking_GET(self):
        Client.objects.create(
            fname='John',
            lname='Doe',
            email='john.doe@example.com',
            cl_password='password',
            phone_number='123456789',
            address='123 Main Street',
        )

        session = self.client.session
        session['type'] = 'client'
        session['username'] = "john.doe@example.com"
        session['password'] = "password"
        session.save()

        response = self.client.get(self.client_tracking_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ClientTracking.html')

    def test_provider_tracking_GET(self):
        Company.objects.create(
            company_name = "Pool Cleaners",
            company_address = "1234 West Street",
            company_phone = "987654321",
            company_email = "pool.cleaners@example.com",
            company_pw = "password"
        )

        session = self.client.session
        session['type'] = 'provider'
        session['username'] = "pool.cleaners@example.com"
        session['password'] = "password"
        session.save()

        response = self.client.get(self.provider_tracking_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProviderTracking.html')