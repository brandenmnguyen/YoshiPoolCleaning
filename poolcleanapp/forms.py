from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import *

# Create a client form
#class ClientForm(ModelForm):
#    class Meta:
#        model = Client
#        fields = ('clientName', 'addressLine', 'postalCode', 'phoneNumber', 'emailAddress')

class ClientForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ('fname', 'lname', 'email', 'cl_password', 'phone_number','address')

    def clean_password(self):
        return self.cleaned_data['password']
        
class ClientUserForm(UserCreationForm):
    fname = forms.CharField(max_length=100, required=False)
    lname = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(max_length=100, required=False, help_text='Enter a valid email address.')
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=255, required = False)

    class Meta(UserCreationForm.Meta):
        model = Client
        fields = ['fname', 'lname', 'email', 'phone_number', 'address', 'password1', 'password2']

    def save(self, commit=True):
        client = super().save(commit=False)
        client.fname = self.cleaned_data['fname']
        client.lname = self.cleaned_data['lname']
        client.phone_number = self.cleaned_data['phone_number']
        client.address = self.cleaned_data['address']
        if commit:
            client.save()
            return client