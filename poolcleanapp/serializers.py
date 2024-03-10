from rest_framework import serializers
from poolcleanapp.models import Client
from poolcleanapp.models import Company
from poolcleanapp.models import Employee
from poolcleanapp.models import Taskping
from poolcleanapp.models import Invoice
from poolcleanapp.models import Appointments


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
   class Meta:
       model = Invoice
       fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  
        fields = '__all__'

class TaskpingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskping
        fields = '__all__'

class AppointmentsSerializer(serializers.ModelSerializer):
 class Meta:
        model = Appointments
        fields = '__all__'