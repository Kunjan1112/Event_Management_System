from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('name/', views.name),

    path('index/', views.index_view, name='index_name'),
    
]
