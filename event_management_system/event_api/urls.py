from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('name/', views.name),

    path('index_view/', views.index_view, name='index_name'),

    path('event_view/', views.event_view, name='event_name'),

    path('about_view/', views.about_view, name='about_name'),

    path('contact_view/', views.contact_view, name='contact_name'),
    
]
