from rest_framework import serializers
from poolcleanapp.models import Client
from poolcleanapp.models import Service
from poolcleanapp.models import Invoice

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service   
        fields = '__all__'    

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice  
        fields = '__all__'   