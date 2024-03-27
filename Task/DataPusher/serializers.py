
from rest_framework import serializers
from .models import Account,Destination




class AccountSerializer(serializers.ModelSerializer):
  
  class Meta:
    
    model=Account
    fields=["email_id","account_id","account_name","website","app_secret_token"]
    extra_kwargs={"app_secret_token":{"read_only":True}}
    
    
class DestinationSerializer(serializers.ModelSerializer):
  
  class Meta:
    
    model=Destination
    
    fields="__all__"
    
class AccountSerializerwithDestination (serializers.ModelSerializer):
  destination=DestinationSerializer(many=True, read_only=True)
  class Meta:
    
    model=Account
    
    fields="__all__"
    
    