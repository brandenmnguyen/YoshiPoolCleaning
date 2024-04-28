from django.test import SimpleTestCase
from django.urls import reverse, resolve
from poolcleanapp.views import homepage, about, clienttracking, providertracking, providerSearch

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

    def test_provider_search_url_resolves(self): #YPS-121 Test 1
        url = reverse('providersearch')
        self.assertEqual(resolve(url).func, providerSearch)

    