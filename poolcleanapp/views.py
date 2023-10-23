from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return render(request, 'hello.html')

def homepage(request):
    return render(request, "Homepage.html")

def login(request):
    return render(request, "LoginPage.html")

def clientSignUp(request):
    return render(request, "ClientSignUp.html")

def providerSignUp(request):
    return render(request, "ProviderSignUp.html")

def providerSearch(request):
    return render(request, "ProviderSearch.html")

def paymentProcessing(request):
    return render(request, "PaymentProcessing.html")

def paymentSuccess(request):
    return render(request, "PaymentSuccess.html")

def clientTracking(request):
    return render(request, "ClientTracking.html")

def providerTracking(request):
    return render(request, "ProviderTracking.html")

def paymentHistory(request):
    return render(request, "PaymentHistory.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

