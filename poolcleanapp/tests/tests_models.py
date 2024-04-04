from django.test import TestCase
from poolcleanapp.models import Client, Company

class TestModels(TestCase):

    def test_model_client(self):
        # create a client model
        client = Client.objects.create(
            fname='John',
            lname='Doe',
            email='john.doe@example.com',
            cl_password='password',
            phone_number='123456789',
            address='123 Main Street',
        )

        self.assertTrue(isinstance(client, Client))

    def test_model_company(self):
        # create a company model
        company = Company.objects.create(
            company_name = "Pool Cleaners",
            company_address = "1234 West Street",
            company_phone = "987654321",
            company_email = "pool.cleaners@example.com",
            company_pw = "password"
        )

        self.assertTrue(isinstance(company, Company))