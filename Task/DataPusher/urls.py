from django import views
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import DestinationView, AccountListCreateView,AccountRetriveUpdateView,incomingView,getDetailsAccountView

router=DefaultRouter()
router.register("DestinationView",DestinationView,basename="DestinationView")
urlpatterns = [
    
    path('AccountListCreateView',AccountListCreateView.as_view(),name="AccountListCreateView"),
    path('AccountRetriveUpdateView/<int:pk>',AccountRetriveUpdateView.as_view(),name="AccountRetriveUpdateView"),
    path('',include(router.urls)),
    path('server/incoming_data/',incomingView.as_view(),name="server/incoming_data"),
    path("getdestinations/<int:pk>",getDetailsAccountView.as_view(),name="to get destinations available for the account")
    
]
