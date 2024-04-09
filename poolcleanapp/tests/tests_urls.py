from django.test import SimpleTestCase
from django.urls import reverse, resolve
from poolcleanapp.views import homepage, about, clienttracking, providertracking

class TestUrls(SimpleTestCase):
    
    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func, homepage)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_client_tracking_url_resolves(self):
        url = reverse('clienttracking')
        self.assertEqual(resolve(url).func, clienttracking)

    def test_provider_tracking_url_resolves(self):
        url = reverse('providertracking')
        self.assertEqual(resolve(url).func, providertracking)