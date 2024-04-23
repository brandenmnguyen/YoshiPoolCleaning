from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import *

# Create a client form
#class ClientForm(ModelForm):
 #   class Meta:
  #      model = Client
   #     fields = ('clientName', 'addressLine', 'postalCode', 'phoneNumber', 'emailAddress')

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


#----------------------INVOICE----------------------------------------------------------
class InvoiceForm(forms.ModelForm):
    card_number = forms.CharField(max_length=16, label='Card Number', required=False)

    class Meta:
        model = Invoice
        fields = ['client', 'c', 'amount', 'payment_method', 'card_name', 'expdate', 'email', 'card_number', 'cvv_code']
    
    # Hidden inputs that will be auto-filled
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget = forms.HiddenInput() 
        self.fields['c'].widget = forms.HiddenInput()
        self.fields['amount'].widget = forms.HiddenInput()

"""
class UpdateTaskpingForm(forms.ModelForm):
    description = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Taskping
        fields = ['status', 'description']

    def save(self, commit=True):
        taskping_instance = super().save(commit=False)
        taskping_instance.description = self.cleaned_data['description']
        taskping_instance.status = self.cleaned_data['status']

        if commit:
            taskping_instance.save()
        return taskping_instance
"""
    
class TaskpingForm(forms.ModelForm):
    class Meta:
        model = Taskping
        fields = ['taskname', 'status', 'description', 'client', 'c_id']  # Including all fields

    def __init__(self, *args, **kwargs):
        super(TaskpingForm, self).__init__(*args, **kwargs)
        self.fields['taskname'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['client'].widget.attrs.update({'class': 'form-control'})
        self.fields['c_id'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        taskping_instance = super().save(commit=False)
        taskping_instance.taskname = self.cleaned_data['taskname']
        if commit:
            taskping_instance.save()
        return taskping_instance


class UpdateAppointmentStatusForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = [] 

    def save(self, commit=True):
        appointment = super().save(commit=False)
        appointment.appstatus = 'Y'  # Set status to 'Y'
        if commit:
            appointment.save()
        return appointment