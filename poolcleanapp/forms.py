from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import *

# Create a client form
#class ClientForm(ModelForm):
    #class Meta:
        #model = Client
        #fields = ('clientName', 'addressLine', 'postalCode', 'phoneNumber', 'emailAddress')

class ProviderForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ('company_name', 'company_address', 'company_phone', 'company_email', 'company_pw')

    def clean_password(self):
        return self.cleaned_data['password']

class ProviderUserForm(UserCreationForm):
    company_name = forms.CharField(max_length=100, required=False)
    company_address = forms.CharField(max_length=255, required=False)
    company_phone = forms.CharField(max_length=20, required=False)
    company_email = forms.EmailField(max_length=100, required=False, help_text='Enter a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = Company
        fields = ['company_name', 'company_address', 'company_phone', 'company_email', 'password1', 'password2']

    def save(self, commit=True):
        company = super().save(commit=False)
        company.company_name = self.cleaned_data['company_name']
        company.company_address = self.cleaned_data['company_address']
        company.company_phone = self.cleaned_data['company_phone']
        if commit:
            company.save()
        return company
