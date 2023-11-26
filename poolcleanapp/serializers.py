from rest_framework import serializers
from poolcleanapp.models import Client
from poolcleanapp.models import Company
#from poolcleanapp.models import Invoice

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
        model = "" 
        fields = '__all__'
