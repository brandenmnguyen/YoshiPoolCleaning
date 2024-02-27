from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('viewClient/', views.getClient, name = 'viewClient'),
    path('viewOneClient/', views.getOneClient),
    path('addClient/', views.addClient, name = 'addClient'),
    path('viewCompany/', views.getCompany, name = 'viewCompany'),
    path('viewOneCompany/', views.getOneCompany),
    path('addCompany/', views.addCompany),
    path('addTaskping/', views.addTaskping),
    path('getTaskping/', views.getTaskping),
    path('viewInvoice/', views.getInvoice),
    path('addInvoice/', views.addInvoice),
    path('add_client/', views.add_client),
    path('viewEmployee/', views.getEmployee),
    path('addEmployee/', views.addEmployee),
    path('deleteEmployee/<int:employee_id>/', views.deleteEmployee),
    path('logout/', views.logout),
    path('getSession/',views.getSession),
    
    path('ping',views.calculate_distance),

    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login_user, name='login'),
    path('providerlogin/', views.login_company, name='providerlogin'),
    path('clientsignup/', views.clientSignUp, name='clientsignup'),
    path('clientlogin/',views.login_client, name='clientlogin'),
    path('viewOneClient/',views.getOneClient, name='viewOneClient'),
    path('providersignup/', views.providerSignUp, name='providersignup'),
    path('providersearch/', views.providerSearch, name='providersearch'),
    path('paymentsuccess/', views.paymentSuccess, name = 'paymentsuccess'),
    path('clienttracking/', views.clienttracking, name='clienttracking'),
    path('providertracking/', views.providertracking, name='providertracking'),
    path('paymenthistory/', views.paymentHistory, name='paymenthistory'),
    path('invoicetracking/', views.invoiceSearch, name='invoicetracking'),
    path('payment/<int:company_id>/<int:client_id>/', views.payment, name='payment'), #TEMPORARY TO GRAB CLIENT can delete later on for next sprint
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar),
    path('dailycalendar/', views.dailycalendar, name='dailycalendar'),
]