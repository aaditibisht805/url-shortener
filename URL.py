#main url file 
from django.contrib import admin
from django.urls import path, include 
from django.http import HttpResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('root.urls'))       # this command leads to the url file created mannually 
]
