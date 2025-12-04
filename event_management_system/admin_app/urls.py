from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('name_view/', views.name_view),

    path('index_view/', views.index_view, name='index_view'),

    path('event_view/', views.event_view, name='event_view'),

    path('user_view/', views.user_view, name='user_view'),
    
]