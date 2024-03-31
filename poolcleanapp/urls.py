from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('viewClient/', views.getClient),
    path('viewOneClient/', views.getOneClient),
    path('addClient/', views.addClient),
    path('viewCompany/', views.getCompany),
    path('viewOneCompany/', views.getOneCompany),
    path('addCompany/', views.addCompany),
    path('viewInvoice/', views.getInvoice),
    path('addInvoice/', views.addInvoice),
    #path('add_client/', views.add_client),
    path('viewEmployee/', views.getEmployee),
    path('addEmployee/', views.addEmployee),
    path('deleteEmployee/<int:employee_id>/', views.deleteEmployee),
    
    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login_user, name = 'login'),
    path('loggin/', views.logging, name = 'logging'),
    path('clientVerification/', views.clientVerification, name='clientVerification'),    
    path('generate_qr_code/', views.generate_qr_code, name = 'generate_qr_code'),
    path('providerlogin/', views.login_company, name = 'providerlogin'),
    path('clientsignup/', views.clientSignUp, name = 'clientsignup'),
    path('providersignup/', views.providerSignUp, name = 'providersignup'),
    path('providersearch/', views.providerSearch, name = 'providersearch'),
    path('paymentsuccess/', views.paymentSuccess),
    path('clienttracking/', views.clienttracking, name = 'clienttracking'),
    path('providertracking/', views.providertracking, name = 'providertracking'),
    path('paymenthistory/', views.paymentHistory, name = 'paymenthistory'),
    #path('invoicetracking/', views.invoiceSearch, name = 'invoicetracking'),
    path('payment/', views.payment, name = 'payment'),
    path('about/', views.about, name = 'about'),
    path('calendar/', views.calendar),
    path('dailycalendar/', views.dailycalendar, name = 'dailycalendar'),

    #------------------------------------------------------------------#
    path('messaging/', views.messaging_view, name='messaging'),
    #------------------------------------------------------------------#
] 