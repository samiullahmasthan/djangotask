from django.shortcuts import render
from .models import Account,Destination

from .serializers import AccountSerializer,DestinationSerializer,AccountSerializerwithDestination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
import requests
# Create your views here.

class AccountListCreateView(ListCreateAPIView):
  
  queryset=Account.objects.all()
  serializer_class=AccountSerializer
  
class AccountRetriveUpdateView(RetrieveUpdateDestroyAPIView):
  
  queryset=Account.objects.all()
  serializer_class=AccountSerializer
  
  def perform_destroy(self, instance):
    Destination.objects.filter(account=instance).delete()
    return super().perform_destroy(instance)
  
class DestinationView(ModelViewSet):
  
  queryset=Destination.objects.all()
  serializer_class=DestinationSerializer
  
  
  
class incomingView(APIView):
  
  def post(self,request):
    print(request,"request")
    if request.method=="POST":
      
      if not request.data or not isinstance(request.data,dict):
        
        return Response({"error":"Invalid Data"})
      
      app_secret_token=request.headers.get('CL-X-TOKEN')
      if not app_secret_token:
        
        return Response({"error":"Unauthenticated token missing"})
      
      try:
        account=Account.objects.get(app_secret_token=app_secret_token)
        
      except Account.DoesNotExist:
        return Response({"error":"Account not found"})
      
      
      for destination in account.destination.all():
        if destination.http_method.lower() =="get":
          
          requests.get(url=destination.url,params=request.data)
        elif destination.http_method.lower() in ["post","put"]:
          requests.post(url=destination.url,json=request.data)
        else:
          return Response({"error":"http method is delete"})
        print("data sending")
        
      return Response({"message":"data sent to destination succefully"})
    
  
    else:
      
      return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  
      
      
class getDetailsAccountView(RetrieveAPIView):
  
  queryset=Account.objects.all()
  
  serializer_class= AccountSerializerwithDestination
      
      
  
  
  

  