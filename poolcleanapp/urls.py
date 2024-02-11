from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('viewClient/', views.getClient),
    path('viewOneClient/', views.getOneClient),
    path('addClient/', views.addClient),
    path('viewService/', views.getService),
    path('addCompany/', views.addCompany),
    path('viewInvoice/', views.getInvoice),
    path('addInvoice/', views.addInvoice),

    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login, name = 'login'),
    path('clientlogin/', views.login_client, name = 'clientlogin'),
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