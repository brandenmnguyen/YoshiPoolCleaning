from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage),
    path('login/', views.login),
    path('clientsignup/', views.clientSignUp),
    path('providersignup/', views.providerSignUp),
    path('providersearch/', views.providerSearch),
    path('paymentprocessing/', views.paymentProcessing),
    path('paymentsuccess/', views.paymentSuccess),
    path('clienttracking/', views.clientTracking),
    path('providertracking/', views.providerTracking),
    path('paymenthistory/', views.paymentHistory),
    path('about/', views.about),
    path('contact/', views.contact),
]