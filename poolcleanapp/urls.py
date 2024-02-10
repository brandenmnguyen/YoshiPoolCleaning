from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('viewClient/', views.getClient),
    path('addClient/', views.addClient),
    path('viewCompany/', views.getCompany),
    path('viewOneCompany/', views.getOneCompany),
    path('addCompany/', views.addCompany),
    path('viewInvoice/', views.getInvoice),
    path('addInvoice/', views.addInvoice),
    path('add_client/', views.add_client),

    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login_user, name = 'login'),
    path('providerlogin/', views.login_company, name = 'providerlogin'),
    path('clientsignup/', views.clientSignUp, name = 'clientsignup'),
    path('providersignup/', views.providerSignUp, name = 'providersignup'),
    path('providersearch/', views.providerSearch, name = 'providersearch'),
    path('paymentsuccess/', views.paymentSuccess),
    path('clienttracking/', views.clienttracking, name = 'clienttracking'),
    path('providertracking/', views.providertracking, name = 'providertracking'),
    path('paymenthistory/', views.paymentHistory, name = 'paymenthistory'),
    path('payment/', views.payment, name = 'payment'),
    path('about/', views.about, name = 'about'),
    path('calendar/', views.calendar),
    path('dailycalendar/', views.dailycalendar, name = 'dailycalendar'),

]