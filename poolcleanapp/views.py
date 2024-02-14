from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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




# Create your views here.

#Rest API
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


@api_view(['GET'])
def getService(request):
    try:
        services = Company.objects.all()  
        serializer = CompanySerializer(services, many=True)  # Serialize the data using the appropriate serializer
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

@api_view(['GET'])
def getInvoice(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addInvoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


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
def providerSignUp(request):
    return render(request, "SignUpProvider.html")

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
    return render(request, "invoice.html")

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