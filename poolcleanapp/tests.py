from django.test import TestCase
from django.urls import reverse
from poolcleanapp.views import payment  # Import the payment view function
from poolcleanapp.models import Company, Client, Invoice
from django.http import HttpRequest


class PaymentViewTest(TestCase):
    def setUp(self):
        # Create a sample company and client for testing
        self.company = Company.objects.create(c_id=1, company_name="Test Company", company_price=100.00)
        self.client = Client.objects.create(client_id=1, fname="John", lname="Doe", email="john.doe@example.com")

    def test_payment_view(self):
        # Create a request object
        request = HttpRequest()
        request.method = 'GET'
        
        # Call the payment view function with the company_id and client_id
        response = payment(request, company_id=self.company.c_id, client_id=self.client.client_id)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the company and client information is passed to the template context
        self.assertIn('company_charges', response.context)
        self.assertIn('company_name', response.context)
        self.assertIn('client_fname', response.context)
        self.assertIn('client_lname', response.context)
        self.assertIn('form', response.context)
