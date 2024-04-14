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
    path('putTaskping/<int:pk>/', views.putTaskping, name='update-taskping-status'),
    path('viewInvoice/', views.getInvoice),
    path('addInvoice/', views.addInvoice),
    path('add_client/', views.add_client),
    path('viewEmployee/', views.getEmployee),
    path('addEmployee/', views.addEmployee),
    path('deleteEmployee/<int:employee_id>/', views.deleteEmployee),
    path('logout/', views.logoutUser, name='logout'),
    path('getSession/',views.getSession),
    #path('messaging/', views.messaging, name = 'messaging'),
    path('viewAppointments/',views.getAppointments),
    path('addAppointments/',views.addAppointments),
    path('viewAvailableAppointments/',views.viewAvailableAppointments),
    path('scheduleAppointments/',views.scheduleAppointment),
    path('sendEmail/',views.send_email),
    path('sendEmailAPI/',views.send_simple_message),
    
    path('ping',views.calculate_distance),
    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login_user, name='login'),
    
    path('clientsignup/', views.clientSignUp, name='clientsignup'),
    
    path('clientVerification/', views.clientVerification, name = 'clientVerification'),
    path('clienttracking/', views.clienttracking, name='clienttracking'),
    path('clientSchedule/', views.clientSchedule, name = 'clientSchedule'),
    path('clientSchedule/schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('viewOneClient/',views.getOneClient, name='viewOneClient'),
    path('providersignup/', views.providerSignUp, name='providersignup'),
    path('providersearch/', views.providerSearch, name='providersearch'),
    path('paymentsuccess/', views.paymentSuccess, name = 'paymentsuccess'),
    
    path('providertracking/', views.providertracking, name='providertracking'),
    path('api/provider-status-update/<int:pk>/', views.update_provider_tracking_status, name='provider-status-update'),
    path('paymenthistory/', views.paymentHistory, name='paymenthistory'),
    path('invoicetracking/', views.invoiceSearch, name='invoicetracking'),
    path('payment/<int:company_id>/<int:client_id>/', views.payment, name='payment'), #TEMPORARY TO GRAB CLIENT can delete later on for next sprint
    path('about/', views.about, name='about'),
    path('verification/', views.verification, name = 'verification'),
    
    path('resultspage/', views.resultspage, name = 'resultspage'),
    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),
    path('calendar/', views.calendar),
    path('dailycalendar/', views.dailycalendar, name='dailycalendar'),
    path('stripeTest/', views.stripeTest, name = 'stripeTest'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('checkout2/', views.checkout2, name = 'checkout2'),
    path('checkout3/', views.checkout3, name = 'checkout3'),
    path('dailycalendarclient/', views.dailycalendarclient, name='dailycalendarclient'),
    path('appView/', views.appointments_view, name = 'appView'),
    path('info/', views.info, name = 'info'),
    

    path('temppaymenthistory/', views.payment_history, name = 'temppaymenthistory'),

    #------------------------------------------------------------------#
    path('messaging/', views.messaging_view, name='messaging'),
    #------------------------------------------------------------------#
] 
