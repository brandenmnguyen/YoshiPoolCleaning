from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse, resolve

class TestViews(TestCase):

    def setUp(self):
        self.client = TestClient()
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
        response = self.client.get(self.client_tracking_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ClientTracking.html')

    def test_provider_tracking_GET(self):
        response = self.client.get(self.provider_tracking_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProviderTracking.html')