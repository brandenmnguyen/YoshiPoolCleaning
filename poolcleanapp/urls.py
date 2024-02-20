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
    path('logout/', views.logoutUser, name='logout'),
    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login_user, name = 'login'),
    path('providerlogin/', views.login_company, name = 'providerlogin'),
    path('loggin/', views.logging, name = 'logging'),
    path('clientsignup/', views.clientSignUp, name = 'clientsignup'),
    path('providersignup/', views.providerSignUp, name = 'providersignup'),
    path('providersearch/', views.providerSearch, name = 'providersearch'),
    path('paymentsuccess/', views.paymentSuccess),
    path('clienttracking/', views.clienttracking, name = 'clienttracking'),
    path('providertracking/', views.providertracking, name = 'providertracking'),
    path('paymenthistory/', views.paymentHistory, name = 'paymenthistory'),
    #path('invoicetracking/', views.invoiceSearch, name = 'invoicetracking'),
    path('payment/', views.payment, name = 'payment'),
    path('verification/', views.verification, name = 'verification'),
    path('about/', views.about, name = 'about'),
    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),
    path('calendar/', views.calendar),
    path('dailycalendar/', views.dailycalendar, name = 'dailycalendar'),

] 