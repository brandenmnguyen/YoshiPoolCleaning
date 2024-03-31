from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import pyotp

#from django.conf import settings
#from django.contrib import messages
#from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from poolcleanapp.models import Client
from poolcleanapp.models import Company
from .models import Company
#from poolcleanapp.models import Invoice
from .serializers import ClientSerializer
from .serializers import CompanySerializer
from .serializers import InvoiceSerializer
from .forms import *
from .serializers import EmployeeSerializer
#from .serializers import InvoiceSerializer
from django.shortcuts import get_object_or_404 ##importing this for getting ID
import qrcode



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

    return Response(company_data, status=status.HTTP_200_OK)

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

def homepage(request):
    return render(request, "Homepage-1.html")

def login_user(request):
    if request.user.is_authenticated:
        return redirect('clienttracking')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password'] 
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('clienttracking')
        else:
            msg = 'Error logging in'
            return render(request, "LoginPage.html", {'msg': msg})
    else:
        return render(request, "LoginPage.html")
    
def login_client(request):
    return render(request, "LoginClientTemp.html")


def login_company(request):
    return render(request, "LoginProvider2.html")

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

    return render(request, "SignUpClientTemp.html")

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

    return render(request, "SignUpProviderTemp2.html")

def providerSearch(request):
    search_term = request.GET.get('search', '')
    info = Company.objects.filter(company_address__icontains=search_term)
    count_results = info.count()
    return render(request, "ResultsPage-1.html", {'info': info, 'count_results': count_results, 'search_term': search_term})
   
   # return render(request, "ResultsPage-1.html")

def payment(request):
    if request.method == "POST":
        if not 'option' in request.POST:
            msg = "Please provide payment option"
            return render(request, "payment_page.html", {'msg': msg})
        option = request.POST['option']
        print(option)
        # temporarily show user input
        if option == "manualCard":
            cardNumber = request.POST['card_number']
            cardName = request.POST['card_name']
            cardExp = request.POST['exp_date']
            cardCCV = request.POST['ccv']
            cardEmail = request.POST['card_email']
            print(cardNumber)
            print(cardName)
            print(cardExp)
            print(cardCCV)
            print(cardEmail)
        # TODO: redirect to payment confirmation
        return render(request, "payment_page.html")
    else:
        return render(request, "payment_page.html")

def paymentSuccess(request):
    return render(request, "PaymentSuccess.html")

#@login_required
def calendar(request):
    return render(request, "calendar.html")

#@login_required
def dailycalendar(request):
    return render(request, "DailyCalendar.html")

#@login_required
def paymentHistory(request):
    return render(request, "Invoice-Tracking/Invoice-Tracking.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

#@login_required
def providertracking(request):
    return render(request, "ProviderTracking.html")

#@login_required
def clienttracking(request):
    return render(request, "ClientTracking.html")

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
            return render(request, 'ClientTracking.html')
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