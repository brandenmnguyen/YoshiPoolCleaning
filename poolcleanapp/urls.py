from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('viewClient/', views.getClient),
    path('addClient/', views.addClient),
    path('viewService/', views.getService),
    path('addCompany/', views.addCompany),
    path('viewInvoice/', views.getInvoice),
    path('addInvoice/', views.addInvoice),
    path('add_client/', views.add_client),

    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage),
    path('login/', views.login_user, name='login'),
    path('clientsignup/', views.clientSignUp),
    path('providersignup/', views.providerSignUp),
    path('providersearch/', views.providerSearch),
    path('paymentsuccess/', views.paymentSuccess),
    path('clienttracking/', views.clienttracking, name='clienttracking'),
    path('providertracking/', views.providertracking),
    path('paymenthistory/', views.paymentHistory),
    path('about/', views.about),
    path('calendar/', views.calendar),
    path('index/', views.index),

]