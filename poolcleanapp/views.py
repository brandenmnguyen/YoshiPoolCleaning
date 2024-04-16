import json
from io import BytesIO
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.http import HttpResponse 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from channels.layers import get_channel_layer

from django.conf import settings
from django.core.serializers import serialize
#from django.conf import settings
#from django.contrib import messages
#from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from poolcleanapp.models import Client
from poolcleanapp.models import Company
from .models import Appointments

from .models import ProviderAvailableTimes             

from .models import Company
#from poolcleanapp.models import Invoice

# serializers.py
from rest_framework import serializers


from .serializers import AppointmentsSerializer, ClientSerializer

from .serializers import ProviderSchedulingSerializer

from .serializers import CompanySerializer
from .serializers import InvoiceSerializer
from .serializers import TaskpingSerializer
from .forms import *
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404 ##importing this for getting ID
from django.http import HttpResponse
from .forms import InvoiceForm
from math import sin, cos, sqrt, atan2, radians
import qrcode
import stripe
from django.contrib import messages
from email.message import EmailMessage
from .models import Taskping
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string

import pyotp

from io import BytesIO

import datetime
import pytz
import smtplib
import ssl
import requests
from django.views.decorators.csrf import csrf_exempt

#from .serializers import ProviderAvailableTimes
#from .serializers import ProviderSchedulingSerializer




# Create your views here.

#Rest API

## --------------- Get Client ----------------
@api_view(['GET'])
def getClient(request):
    try:
        clients = Client.objects.all()  # Replace YourModel with your actual model
        serializer = ClientSerializer(clients, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def getOneClient(request):
    email = request.GET.get('email')
    cl_password = request.GET.get('cl_password')

    try:
        client = Client.objects.get(email=email, cl_password = cl_password)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=404)
    
    client_data = {
        'fname': client.fname,
        'lname': client.lname,
        'phone_number': client.phone_number,
        'email': client.email,
        'cl_password': client.cl_password,
        'address': client.address,
    }
    request.session['username'] = client.email
    request.session['password'] = client.cl_password
    request.session['type'] = "client"

    return Response(client_data, status=status.HTTP_200_OK)

## --------------- Create Cilent ----------------
@api_view(['POST'])
def addClient(request):
    try:
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## --------------- Get Service ----------------

@api_view(['GET'])
def getCompany(request):
    try:
        services = Company.objects.all()  
        serializer = CompanySerializer(services, many=True)  # Serialize the data using the appropriate serializer
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def getOneCompany(request):
    # Get parameters from the request
    company_email = request.GET.get('company_email')
    company_pw = request.GET.get('company_pw')

    # Perform the query to get the company
    try:
        company = Company.objects.get(company_email=company_email, company_pw=company_pw)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=404)
    
    # Serialize the company data if needed
    company_data = {
        'company_name': company.company_name,
        'company_address': company.company_address,
        'company_phone': company.company_phone,
        'company_email': company.company_email,
        'company_pw': company.company_pw,
    }
    
    request.session['username'] = company.company_email
    request.session['password'] = company.company_pw
    request.session['type'] = "provider"

    return Response(company_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getSession(request):

    if not 'username' in request.session and not 'password' in request.session:
        return Response("user not logged in", status=status.HTTP_404_NOT_FOUND)
    
    username = request.session['username']
    password =  request.session['password']
    type = request.session['type']

    user_data = {
        'username': username,
        'password': password,
        'type': type,
    }
    return Response(user_data, status=status.HTTP_200_OK)

## --------------- Create Company ----------------
@api_view(['POST'])
def addCompany(request):
    try:
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
## --------------- Create Taskping ----------------
@api_view(['POST'])
def addTaskping(request):
    try:
        serializer = TaskpingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
## --------------- GET Taskping ----------------
@api_view(['POST'])
def addTaskping(request):
    try:
        serializer = TaskpingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
## --------------- GET Taskping ----------------
@api_view(['GET'])
def getTaskping(request):
    try:
        taskpings = Taskping.objects.all()  # Ensure Taskping is your model name
        serializer = TaskpingSerializer(taskpings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## --------------- Put Taskping ----------------
from asgiref.sync import async_to_sync
@api_view(['PUT', 'POST'])  # Using PUT for update operations, POST can be used for creating
def putTaskping(request, pk):
    try:
        task = Taskping.objects.get(pk=pk)
        # Restrict updates to the 'status' field only
        serializer = TaskpingSerializer(task, data={'status': request.data.get('status')}, partial=True)
        serializer = TaskpingSerializer(task, data={'description': request.data.get('description')}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Taskping.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## --------------- Get Invoice ----------------
@api_view(['GET'])
def getInvoice(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

## --------------- Create Invoice ----------------
@api_view(['POST'])
def addInvoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

## --------------- Create Employee ----------------
@api_view(['POST'])
def addEmployee(request):
    try:
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
## --------------- get Employee ----------------
def getEmployeeId(employee_id): ##getter for employee ID
    return get_object_or_404(Employee, employee_id=employee_id) 

@api_view(['GET'])
def getEmployee(request):
    try:
        employees = Employee.objects.all()  
        serializer = EmployeeSerializer(employees, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
## --------------- delete Employee ----------------
    

@api_view(['DELETE','GET'])
def deleteEmployee(request, employee_id):
    try:
        employee = getEmployeeId(employee_id=employee_id)
        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#Anonymous required
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'Homepage'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator

## --------------- Appointment Scheduling ----------------
#get only 1 appointment details
@api_view(['GET'])
def getAppointmentDetails(request, pk):
    try:
        appointment = Appointments.objects.get(pk=pk)  # Use get() and catch DoesNotExist
        serializer = AppointmentsSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Appointments.DoesNotExist:
        return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
@api_view(['GET'])
def getAppointments(request):
    try:
        services = Appointments.objects.all()  
        serializer = AppointmentsSerializer(services, many=True)  # Serialize the data using the appropriate serializer
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def addAppointments(request):
    try:
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def viewAvailableAppointments(request):
    # Get parameters from the request
    appdate = request.data.get('appdate')
    c = request.data.get('c')

    available_appointments = Appointments.objects.filter(c=c, appdate=appdate)

    # Extract appointment times from available appointments
    appointment_times = [appointment.apptime.strftime('%H:%M') for appointment in available_appointments]

    # Sort the appointment times
    appointment_times.sort()

    # Return the list of appointment times
    return Response(appointment_times, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def scheduleAppointment(request):
    # Get parameters from the request
    appdate = request.data.get('appdate')
    apptime = request.data.get('apptime')
    c = request.data.get('c')

    # Perform the query to check if appointment exists
    try:
        appointment = Appointments.objects.get(appdate=appdate, apptime=apptime, c=c)
        return Response({'error': 'Appointment already scheduled'}, status=404)
    except Appointments.DoesNotExist:
        # If appointment does not exist, add it
        try:
            serializer = AppointmentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


## --------------- Notifications ----------------  

@api_view(['POST'])
def send_email(request):
    data = json.loads(request.body)
    print(data)

    email_sender = "do.not.reply2.poolcleaningapp@gmail.com"
    email_pass = "ntnqmfmbcoswvbvb"

    #email_receiver = "mohammedalch1111@gmail.com"
    email_receiver = request.data.get('email')

    #email_subject = "subject2"
    email_subject = request.data.get('subject')

    body = request.data.get('body')

    email_message = EmailMessage()
    email_message['From'] = email_sender
    email_message['To'] = email_receiver
    email_message['Subject'] = email_subject
    email_message.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_sender,email_pass)
        smtp.sendmail(email_sender,email_receiver,email_message.as_string())
        smtp.quit()

    return Response(request.data, status=status.HTTP_200_OK)

@csrf_exempt 
@api_view(['POST'])
def send_simple_message(request):
    email_receiver = request.data.get('email')
    email_subject = request.data.get('subject')
    body = request.data.get('body')

    r = requests.post(
		"https://api.mailgun.net/v3/sandboxceea637047d742199cae2aa88cf4a967.mailgun.org/messages",
		auth=("api", "c77ac05298d93c5f5f06d32f4ca8f16e-f68a26c9-0a1e5bb7"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxceea637047d742199cae2aa88cf4a967.mailgun.org>",
			"to": "Mohammed Al Chalabi <"+email_receiver+">",
			"subject": email_subject,
			"text":body})
    return Response(request.data, status=r.status_code)  



@api_view(['GET'])
def getProviderSchedule(request):
    try:
        provSchedule = ProviderAvailableTimes.objects.all()  # Replace YourModel with your actual model
        serializer = ProviderSchedulingSerializer(provSchedule, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def addProviderAppointments(request):
    try:
        serializer = ProviderSchedulingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    





@api_view(['POST'])
def scheduleProvAppointment(request):
    # Get parameters from the request
    appdate = request.data.get('appdate')
    apptime = request.data.get('apptime')
    c_id = request.data.get('c_id')

    # Perform the query to check if appointment exists
    try:
        appointment = ProviderAvailableTimes.objects.get(appdate=appdate, apptime=apptime, c_id=c_id)
        return Response({'error': 'Appointment already scheduled'}, status=404)
    except ProviderAvailableTimes.DoesNotExist:
        # If appointment does not exist, add it
        try:
            serializer = ProviderSchedulingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



































def homepage(request):
    return render(request, "Homepage-1.html")

#, 'appdate': appointments.appdate, 'appetite': appointments.appetime

def appointments_view(request):

    appointments = Appointments.objects.all()
    appointment_data = [{'appdate':  appointment.appdate.strftime('%Y-%m-%d'), 'apptime': appointment.apptime.strftime('%H:%M:%S') } for appointment in appointments]
    request.session['appointments'] = appointment_data


    return render(request, 'ClientCalendarClient.html', {'appointments': appointments})





#for QR code generator 
def generate_qr_code(request):
    if request.method == 'GET':
        # The secret key used to generate TOTP codes
        key = 'base32secret3232'

        # Generate the TOTP code using the secret key
        totp = pyotp.TOTP(key)

        # Generate the provisioning URI for the QR code
        uri = totp.provisioning_uri(name='poolUser', issuer_name='poolUser')

        # Generate the QR code image
        qr = qrcode.make(uri)

        # Create a BytesIO object to store the image data
        img_buffer = BytesIO()
        qr.save(img_buffer)
        img_buffer.seek(0)

        # Return the image data as an HTTP response
        return HttpResponse(img_buffer.getvalue(), content_type='image/png')
    else:
        # Handle other HTTP methods (e.g., POST)
        return HttpResponse("Method not allowed", status=405)


#For two factor authentication

def verification(request):
    if request.method == 'POST':
        user_totp_code = request.POST.get('totp_code')  # Assuming the form field is named 'totp_code'

        # The secret key used to generate TOTP codes
        key = 'base32secret3232'

        # Generate the TOTP code using the secret key
        totp = pyotp.TOTP(key)
        generated_totp_code = totp.now()



        # Compare the user-entered TOTP code with the generated TOTP code
        if user_totp_code == generated_totp_code:
            # TOTP code is correct
            return redirect( 'providertracking')
        else:
            # TOTP code is incorrect
            return render(request, 'LoginPage.html')

    # Handle GET request or other cases
    return render(request, 'verification_form.html')

#for messaging
def messaging(request):
    room = Chat.objects.filter(cl=1).first()
    chats = []  
    return render(request, 'messaging.html', {'room' : room, 'chats': chats})

def login_user(request):
 #   if request.user.is_authenticated:
  #      return redirect('clienttracking')
   # if request.method == "POST":
    #    email = request.POST['email']
     #   password = request.POST['password'] 
      #  user = authenticate(request, username=email, password=password)
       # if user is not None:
        #    login(request, user)
         #   return redirect('clienttracking')
        #else:

         #   messaging = 'Email or password is incorrect'
          #  return render(request, "LoginPage.html", {'msg': messaging})
    #else:
        return render(request, "LoginPage.html")
    



def login_client(request):
    return render(request, "LoginClientTemp.html")



def logging(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password') 
        if email and password:  # Check if both email and password are provided
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('clienttracking')
            else:
                messaging = 'Email or password is incorrect'
        else:
            messaging = 'Email and password are required'
        return render(request, "LoginPage.html", {'msg': messaging})
    else:
        return render(request, "LoginPage.html")



def login_company(request):
    return render(request, "LoginProvider2.html")

# Logs out the user whether client or provider
@api_view(['DELETE','GET'])
def logout(request):
    request.session.flush()
    return redirect('homepage')

@anonymous_required
def clientSignUp(request, *args, **kwargs):
    if request.POST:
        form = ClientForm(request.POST) 
        print("Submitted data:", request.POST)
        if form.is_valid():
            print("Submitted form data:", form.cleaned_data)
            client = form.save()
        else:
            form = ClientForm()

    return render(request, "SignUpClient.html")

@anonymous_required
def invoiceSearch(request):
    return render(request, "InvoiceTracking.html")

@anonymous_required
def add_client(request):
    form = ClientForm()
    return render(request, "add_client.html", {'form': form})

@anonymous_required
def providerSignUp(request, *args, **kwargs):
    
    if request.POST:
        form = ProviderForm(request.POST)
        print("Submitted data:", request.POST)
        if form.is_valid():
            print("Submitted form data:", form.cleaned_data)
            provider = form.save()
        #print(form)
    else:
        form = ProviderForm()

    return render(request, "SignUpProvider.html")

@anonymous_required
def invoiceSearch(request):
    return render(request, "InvoiceTracking.html")

#@login_required(login_url=logging)
def providerSearch(request):
    search_term = request.GET.get('search', '')
    info = Company.objects.filter(company_address__icontains=search_term)
    count_results = info.count()
    return render(request, "ResultsPage-1.html", {'info': info, 'count_results': count_results, 'search_term': search_term})
   
    #return render(request, "ResultsPage-1.html")


## --------------- PAYMENT PAGE ---------------------------------------------------------------------------

def getCompanyPrice(c_id): # GET COMPANY
    company = get_object_or_404(Company, C_id=c_id)
    return company.company_price

def getClientName(client_id):
    client = get_object_or_404(Client, id=client_id)
    return client.fname, client.lname 

def payment(request, company_id, client_id):
    try:
        # Retrieve the company price based on the provided company ID
        company = Company.objects.get(c_id=company_id)
        company_charges = company.company_price
        company_name = company.company_name  # Get the company name

        # Get client information
        client = Client.objects.get(client_id=client_id)
        client_fname = client.fname
        client_lname = client.lname

        if request.method == 'POST':
            # If the request method is POST, process the form data
            form = InvoiceForm(request.POST)
            if form.is_valid():
                # If form is valid, save the invoice and redirect
                invoice = form.save()
                return HttpResponse('Invoice created successfully!')
        else:
            # Create an instance of the invoice form and pre-fill it with relevant data
            initial_data = {
                'client': client_id,
                'c': company_id,
                'amount': company_charges,
                'email': client.email  # You can pre-fill other fields as needed
            }
            form = InvoiceForm(initial=initial_data)

        # Pass company charges, company name, client information, and the invoice form to the template
        return render(request, "payment_page.html", {'company_charges': company_charges, 'company_name': company_name, 'client_fname': client_fname, 'client_lname': client_lname, 'form': form})
    except Company.DoesNotExist:
        msg = "Company not found"
        return render(request, "payment_page.html", {'msg': msg})
    except Client.DoesNotExist:
        msg = "Client not found"
        return render(request, "payment_page.html", {'msg': msg})



def paymentSuccess(request):
    return render(request, "paymentsuccessful.html")

## ------------------------------------------------------------------------------------------

@api_view(['POST'])
def calculate_distance(request):
   
    data = json.loads(request.body)
    print(data)
    lat1 = float(data['lat1'])
    lon1 = float(data['lon1'])
    lat2 = float(data['lat2'])
    lon2 = float(data['lon2'])
    
    distance = haversine_distance(lat1, lon1, lat2, lon2)

    if distance > 0.1:
        message = 'Provider is ' + str(round(distance, 2)) + ' miles away'
        return Response(message,status=status.HTTP_404_NOT_FOUND)
    else:
        return Response("Provider has arrived!",status=status.HTTP_200_OK)
    
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 3959.0  # Earth's radius in miles
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

#@login_required
#@login_required(login_url=logging)
def calendar(request):
    return render(request, "calendar.html")

#@login_required
#@login_required(login_url=logging)
def dailycalendar(request):
    company_email = request.session.get('username')
    company_pw = request.session.get('password')
    company = getCompanyLogin(company_email, company_pw)
    if company is None:
        return render (request, "ErrorPage.html", {'error': 'Company not found.'})
    
    appointments = Appointments.objects.filter(c_id=company.c_id)  
    data = [{
        'cname': appointment.cl.fname + " " + appointment.cl.lname,
        'appdate':  appointment.appdate.strftime('%m/%d/%Y'), 
        'apptime': appointment.apptime.strftime('%H:%M') 
    } for appointment in appointments]
    
    return render(request, "DailyCalendar.html", {'appointments': data})


def dailycalendarclient(request):
    return render(request, "ClientCalendarClient.html")

#@login_required
#@login_required(login_url=logging)
def paymentHistory(request):
    return render(request, "InvoiceTracking.html")





def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
#-----------------------TRACKING PAGE------------------------------------
#@login_required
#@login_required(login_url=login_user)
""""
@api_view(['GET'])
def getOneCompany(request, pk):
    try:
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
"""

@api_view(['GET'])
def getTaskpingFrom(request,companyID,clientID):
    try:
        taskpings = Taskping.objects.filter(c_id = companyID, client = clientID) 
        serializer = TaskpingSerializer(taskpings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def getOneClient(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def getCompanyLogin(company_email, company_pw):
    try:
        company = Company.objects.get(company_email=company_email, company_pw=company_pw)
        return company
    except Company.DoesNotExist:
        return None

"""  old providertracking view
def providertracking(request, form=None):
    company_email = request.session.get('username')
    company_pw = request.session.get('password')
    company = getCompanyLogin(company_email, company_pw)
    if company is None:
        return render(request, "ErrorPage.html", {'error': 'Company not found'})

    company_id = company.c_id
    appointment_list = Appointments.objects.filter(c=company_id)
    tasks = Taskping.objects.filter(c_id=company_id)

    if not form:
        form = TaskpingForm()  # Create a new form if one isn't passed

    context = {
        'company': company,
        'appointment_list': appointment_list,
        'form': form,
        'tasks': tasks,
    }

    return render(request, "ProviderTracking.html", context)
"""
@csrf_exempt
def submit_task_form(request, companyID, clientID):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.get(pk=companyID)
            client = Client.objects.get(pk=clientID)
        except (Company.DoesNotExist, Client.DoesNotExist):
            return JsonResponse({'status': 'error', 'message': 'Company or Client not found'}, status=404)

        for taskname in data.get('tasknames', []):
            Taskping.objects.create(
                taskname=taskname,
                status=data.get('status', 'n'),  # Default to 'n' if status not provided
                description=data.get('description', ''),  # Default to empty string if description not provided
                client=client,
                c_id=company
            )

        return JsonResponse({'status': 'success', 'message': 'Tasks submitted successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@csrf_exempt
def update_task(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Taskping.objects.get(pk=task_id)
        task.status = data['status']
        task.description = data['description']
        task.save()
        return JsonResponse({'message': 'Task updated successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)
@require_http_methods(["GET", "POST"])  # Ensure only GET and POST requests are accepted

def providertracking(request):
    task_list = Taskping.objects.filter(c_id=1)   # as an example
    if 'username' in request.session:
        account_name = request.session['username']
    else:
        account_name = "account_name"
    
    context = {
        'task_list': task_list,
        'account_name': account_name,
    }
    return render(request, "ProviderTracking.html", context)


#@login_required
#@login_required(login_url=login_user)
"""def clienttracking(request):
    task_list = Taskping.objects.filter(client=1)   #need to replace with logged in client
    return render(request, "ClientTracking.html", {'task_list': task_list})
"""



#DISPLAYING AVAILABLE TIME OF PROVIDER
def clientSchedule(request):
    schedule_list = ProviderAvailableTimes.objects.filter(c_id=24)   
    return render(request, "clientSchedule.html", {'schedule_list': schedule_list})



#SHOW APPOINTMENT INFO FOR CLIENT 
def info(request):
 
    appointments = Appointments.objects.filter(cl_id=3)   
    appointment_data = [{'appdate':  appointment.appdate.strftime('%Y-%m-%d'), 'apptime': appointment.apptime.strftime('%H:%M:%S') } for appointment in appointments]
    request.session['appointments'] = appointment_data

    return render(request, 'viewInfo.html', {'appointments': appointments})


#SCHEDULING LOGIC
def schedule_appointment(request):
    if request.method == 'POST':
        # Parse JSON data from request body
        data = json.loads(request.body)
      #  cl_id = data.get('cl_id')
       # c_id = data.get('c_id')
        c_id = int(data.get('c_id'))  # Convert c_id to an integer
        appdate = data.get('appdate')
        apptime = data.get('apptime')


        # Check if appointment already exists
        if Appointments.objects.filter(c_id=c_id, appdate=appdate, apptime=apptime).exists():
            return JsonResponse({'error': 'Appointment already scheduled.'}, status=400)


        # Create a new appointment instance
        appointment = Appointments( c_id=c_id, appdate=appdate, apptime=apptime)
        
        # Save the appointment to the database
        appointment.save()

        # Return a success response
        return JsonResponse({'message': 'Appointment scheduled successfully.'})
    else:
        # Return an error response if method is not POST
        return JsonResponse({'error': 'Invalid request method.'}, status=400)





def ScheduleTimingProvider(request):
    return render(request, "ScheduleTimingProvider.html")


#save info that the provider entered for available dates and estimated times
def providerDateTimeScheduling(request):
    if request.method == 'POST':

          # Retrieve data from the form
       # c_id = request.POST.get('c_id')
        c_id = int(request.POST.get('c_id'))
        appdate = request.POST.get('date')
        apptime = request.POST.get('time')

        # Create a new appointment instance
        provAppointment = ProviderAvailableTimes(c_id=c_id, appdate=appdate, apptime=apptime)

        # Save the appointment to the database
        provAppointment.save()
        # Return a success response
        return JsonResponse({'message': 'Appointment scheduled successfully.'})
    else:
        # Return an error response if method is not POST
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



# def clientSchedule(request):
    # Assuming 'cl' is a key associated with the client's ID in the session
    # client_id = request.session.get('cl')

    # If client_id is None, it means the client is not logged in or the session doesn't contain their ID
    # if client_id is None:
        # You can handle this case as per your application's requirements
        # return HttpResponse("You need to log in to view the schedule.")

    # Assuming Appointments model has a field 'client_id' representing the client associated with the appointment
    # schedule_list = Appointments.objects.filter(client_id=client_id)

    # return render(request, "clientSchedule.html", {'schedule_list': schedule_list})





#--------------------- LOGIN --------------------------------------
def logging(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password') 
        if email and password:  # Check if both email and password are provided
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('clienttracking')
            else:
                messaging = 'Email or password is incorrect'
        else:
            messaging = 'Email and password are required'
        return render(request, "LoginPage.html", {'msg': messaging})
    else:
        return render(request, "LoginPage.html")
    

def clientVerification(request):
    if request.method == 'POST':
        user_totp_code = request.POST.get('totp_code')

        key = 'base32secret3232'

        totp = pyotp.TOTP(key)
        generated_totp_code = totp.now()

        if user_totp_code == generated_totp_code:
            return redirect('clienttracking')
        else:
            return render(request, 'LoginPage.html')

    return render(request, 'ClientVerification.html')

def generate_qr_code(request):
    if request.method == 'GET':
        key = 'base32secret3232'

        totp = pyotp.TOTP(key)
        uri = totp.provisioning_uri(name='poolUser', issuer_name='poolUser')

        qr = qrcode.make(uri)

        img_buffer = BytesIO()
        qr.save(img_buffer)
        img_buffer.seek(0)

        return HttpResponse(img_buffer.getvalue(), content_type='image/png')
    else:
        return HttpResponse("Method not allowed", status=405)


from django.shortcuts import render

def messaging_view(request):
    return render(request, 'messaging.html')


# Stripe

def stripeTest(request):
    return render(request, "stripeTest.html")

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1On6V4FamngtG7BE9RUVZhNs',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/poolcleanapp/clienttracking/',
        cancel_url='http://127.0.0.1:8000/poolcleanapp/clienttracking/',
    )

    return redirect(checkout_session.url, code=303)

def checkout2(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1OsJnIFamngtG7BEWNIUWEqY',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/poolcleanapp/clienttracking/',
        cancel_url='http://127.0.0.1:8000/poolcleanapp/clienttracking/',
    )

    return redirect(checkout_session.url, code=303)

def checkout3(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1OsJo8FamngtG7BE9w7XfgRm',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/poolcleanapp/clienttracking/',
        cancel_url='http://127.0.0.1:8000/poolcleanapp/clienttracking/',
    )

    return redirect(checkout_session.url, code=303)

def payment_history(request):
    session_id = request.session.session_key
    user_id = request.session.get('username')
    if not user_id:
        return HttpResponse("User not logged in or user_id not set", status=400)
    payment_intent_id = "pi_3P0WfpFamngtG7BE057myOwA"
    payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    # payment_intents = stripe.PaymentIntent.list(customer=user_id)
    amount_in_dollars = "{:.2f}".format(payment_intent.amount / 100)
    timestamp = payment_intent.created
    dt_utc = datetime.datetime.utcfromtimestamp(timestamp)
    pst_timezone = pytz.timezone('America/Los_Angeles')
    dt_pst = dt_utc.replace(tzinfo=pytz.utc).astimezone(pst_timezone)
    return render(request, 'temp_payment_history.html', {'payment_intent': payment_intent, 'amount_in_dollars': amount_in_dollars, 'dt_pst': dt_pst})

#End of Stripe

# Client/Provider Settings Page

def clientSettings(request):
    session_id = request.session.session_key
    user_id = request.session.get('username')
    if not user_id:
        return HttpResponse("User not logged in or user_id not set", status=400)
    user_pass = request.session.get('password')
    try:
        client = Client.objects.get(email=user_id)
        client_id = client.client_id
    except Client.DoesNotExist:
        client_id = None
    print('user id:', client_id)
    return render(request, 'clientSettings.html', {'user': user_id, 'pass': user_pass, 'client_id': client_id}, )

@api_view(['PUT'])
def updateClient(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
        serializer = ClientSerializer(instance=client, data=request.data)
        if 'email' in request.data:
            new_email = request.data['email']
            # Check if the new email is already in use
            existing_client = Client.objects.filter(email=new_email).exclude(pk=client_id).first()
            if existing_client:
                return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def companySettings(request):
    session_id = request.session.session_key
    user_id = request.session.get('username')
    if not user_id:
        return HttpResponse("User not logged in or user_id not set", status=400)
    user_pass = request.session.get('password')
    try:
        company = Company.objects.get(company_email=user_id)
        company_id = company.c_id
    except Client.DoesNotExist:
        company_id = None
    return render(request, 'providerSettings.html', {'user': user_id, 'pass': user_pass, 'company_id': company_id}, )

@api_view(['PUT'])
def updateCompany(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if 'company_email' in request.data:
            new_email = request.data['company_email']
            # Check if the new email is already in use
            existing_company = Company.objects.filter(company_email=new_email).exclude(pk=company_id).first()
            if existing_company:
                return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# End of Client/Provider Settings Page

#logout
def logoutUser(request):
    logout(request)
    return redirect(login_user)

#@login_required
def resultspage(request):
    return render(request, "ResultsPage-1.html")


#def index(request):
    #context = {}
    #return render(request, 'invoice/index.html', context)


#@login_required
#def clients(request):
    #context = {}
    #clients = Client.objects.all()
    #context['clients'] = clients

    #if request.method == 'GET':
     #   form = ClientForm()
      #  context['form'] = form
       # return render(request, 'invoice/clients.html', context)

    #if request.method == 'POST':
     #   form = ClientForm(request.POST, request.FILES)

      #  if form.is_valid():
       #     form.save()

        #    messages.success(request, 'New Client Added')
         #   return redirect('clients')
        #else:
         #   messages.error(request, 'Problem processing your request')
          #  return redirect('clients')


    #return render(request, 'invoice/clients.html', context)




#@login_required
#def createInvoice(request):
    #create a blank invoice ....
   # number = 'INV-'+str(uuid4()).split('-')[1]
   # newInvoice = Invoice.objects.create(number=number)
    #newInvoice.save()

    #inv = Invoice.objects.get(number=number)
    #return redirect('create-build-invoice', slug=inv.slug)
def getClientName(email, cl_password):
    try:
        client = Client.objects.get(email=email, cl_password=cl_password)
        return client
    except Client.DoesNotExist:
        return None

def getProviderIdFromClient(client_id):
    try:
        # Attempt to get the first Taskping instance matching the client_id
        taskping_instance = Taskping.objects.filter(client_id=client_id).first()

        # If a Taskping instance is found, return its associated company's c_id
        if taskping_instance:
            return taskping_instance.c_id_id  # Assuming c_id is the ForeignKey to the Company
        else:
            return None
    except Taskping.DoesNotExist:
        # This exception block may actually never be hit because .first() will return None
        # instead of raising DoesNotExist if no objects match the filter
        return None

        #@login_required
#@login_required(login_url=login_user)
def clienttracking(request):
    email = request.session.get('username')  # Assuming email is stored in the session
    cl_password = request.session.get('password')  # Assuming password is stored in the session
    client = getClientName(email, cl_password)
    if client is None:
        return render(request, "ErrorPage.html", {'error': 'Client not found'})

    client_id = client.client_id
    c_id = getProviderIdFromClient(client_id)  # Fetch company ID using the client ID

    appointment_list = Appointments.objects.filter(cl = client_id)
    task_list = Taskping.objects.filter(client=client)  # Filter Taskping objects by client object

    company = None
    if c_id:
        try:
            company = Company.objects.get(c_id=c_id)  # Attempt to get the Company object using c_id
        except Company.DoesNotExist:
            company = None  # Handle the case where no Company matches the c_id

    context = {
        'appointment_list': appointment_list,
        'client': client,
        'company': company,  # Pass the company object, which may be None
        'task_list': task_list,  # Pass the list of tasks associated with the client
    }
    return render(request, "ClientTracking.html", context)

def editAccount(request):
    # Corrected the typo in 'request'
    password = request.session.get('password')
    email = request.session.get('username')
    client=Client.objects.get(email=email,cl_password=password)
    context={
        'client': client
    }
    # Use 'render' function to render the 'editAccount.html' template with context
    return render(request, "editAccount.html",context)
    

def update_client_field(request, client_id):
    try:
        client = Client.objects.get(client_id=client_id)  # Corrected field name
        if request.method == 'POST':
            form = ClientUpdateForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success', 'message': 'Field updated successfully'})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
    except Client.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Client not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@api_view(['GET'])
def getClienttDetails(request, pk):
    try:
        appointment = Client.objects.get(pk=pk)  # Use get() and catch DoesNotExist
        serializer = ClientSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)