from django import forms
from django.forms import ModelForm
from .models import Client

# Create a client form
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('clientName', 'addressLine', 'postalCode', 'phoneNumber', 'emailAddress')