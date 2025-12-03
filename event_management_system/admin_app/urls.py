from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('name_view/', views.name_view),
    
]