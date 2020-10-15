from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('studdist.urls')),
    path('', include('frontend.urls')),

    
]
