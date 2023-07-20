#url file defined inside root folder
from django.urls import path
from .views import createUrl,routeToURL
from django.http import HttpResponse

urlpatterns = [
   
    path('',createUrl), 
    path('<slug:key>/', routeToURL)
]  
