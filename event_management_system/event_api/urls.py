from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('name/', views.name),

    path('index/', views.index, name='index'),

    path('event/', views.event, name='event'),

    path('about/', views.about, name='about'), 

    path('contact/', views.contact, name='contact'),
    
]
