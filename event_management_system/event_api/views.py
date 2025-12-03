from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name(request):
    return HttpResponse("Hello World!")

def index_view(request):
    return render(request, 'index.html')

def event_view(request):
    return render(request, 'event.html')

def about_view(request):
    return render(request, 'about.html')