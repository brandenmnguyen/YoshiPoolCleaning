from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('viewClient/', views.getClient, name = 'viewClient'),
    path('viewOneClient/', views.getOneClient),
    path('addClient/', views.addClient, name = 'addClient'),
    path('updateClient/<int:client_id>/', views.updateClient, name = 'updateClient'),
    path('viewCompany/', views.getCompany, name = 'viewCompany'),
    path('viewOneCompany/', views.getOneCompany),
    path('addCompany/', views.addCompany),
    path('updateCompany/<int:company_id>/', views.updateCompany, name = 'updateCompany'),
    path('addTaskping/', views.addTaskping),

    path('getProviderSchedule/', views.getProviderSchedule),
    path('addProviderSchedule/', views.addProviderAppointments),
    path('scheduleProvAppointments/',views.scheduleProvAppointment),


    path('getTaskping/', views.getTaskping),
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

    path('editaccount/getClientDetails/<int:pk>/', views.getClienttDetails, name='get_client_details'), 
    path('editaccount/',views.editAccount, name='editAccount'),
    path('editaccount/update/<int:client_id>/', views.update_client_field, name='update_client'),

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
    
    path('providertracking/', views.providertracking, name='providertracking'),
    #path('api/provider-status-update/<int:pk>/', views.update_provider_tracking_status, name='provider-status-update'),
    path('paymenthistory/', views.payment_history, name='paymenthistory'),
    path('about/', views.about, name='about'),
    path('verification/', views.verification, name = 'verification'),
    
    path('resultspage/', views.resultspage, name = 'resultspage'),
    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),
    path('calendar/', views.calendar),
    path('dailycalendar/', views.dailycalendar, name='dailycalendar'),
    path('paymentpage/', views.paymentPage, name = 'paymentpage'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('checkout2/', views.checkout2, name = 'checkout2'),
    path('checkout3/', views.checkout3, name = 'checkout3'),
    path('dailycalendarclient/', views.dailycalendarclient, name='dailycalendarclient'),
    path('appView/', views.appointments_view, name = 'appView'),
    path('info/', views.info, name = 'info'),
    path('clientSchedule/', views.clientSchedule, name = 'clientSchedule'),
    path('clientSchedule/schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('ScheduleTimingProvider/', views.ScheduleTimingProvider, name='ScheduleTimingProvider'),
    path('ScheduleTimingProvider/providerDateTimeScheduling/', views.providerDateTimeScheduling, name='providerDateTimeScheduling'),
    path('temppaymenthistory/', views.payment_history, name = 'temppaymenthistory'),
    path('clientSettings/', views.clientSettings, name = 'clientSettings'),
    path('providerSettings/', views.companySettings, name = 'providerSettings'),
    path('client_Schedule/<int:pk>/', views.client_Schedule, name='client_Schedule'),
    path('client_Schedule/<int:pk>/schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    #------------------------------------------------------------------#
    path('messaging/', views.messaging_view, name='messaging'),
    #------------------------------------------------------------------#
    path('ProviderTracking/getAppointmentDetails/<int:pk>/', views.getAppointmentDetails, name='get_appointment_details'),
    #path('ProviderTracking/getOneAppointment/<int:pk>/', views.getOneAppointment, name='getOneAppointment'),
    #path('ProviderTracking/company/<int:pk>/', views.getOneCompany, name='get-one-company'),
    path('ProviderTracking/client/<int:pk>/', views.getOneClient1, name='get-one-client'),
    path('ProviderTracking/submit_task/<int:companyID>/<int:clientID>/', views.submit_task_form, name='submit_task_form'),
    path('ProviderTracking/taskping/<int:companyID>/<int:clientID>/', views.getTaskpingFrom, name='getTaskpingFrom'),
    path('ProviderTracking/updateTask/<int:task_id>/', views.update_task, name='update_task'),
    path('putTaskping/<int:pk>/', views.putTaskping, name='update-taskping-status'),
    #path('client-tracking/<int:pk>/', views.clienttrackingWithout, name='client-tracking'),
    path('ProviderTracking/update_appstatus/<int:appointment_id>/', views.update_appstatus, name='update_appstatus'),
    path('ProviderTracking/deleteAllTaskpings/<int:clientId>/<int:companyId>/', views.deleteAllTaskpings, name='delete_all_taskpings'),
]

