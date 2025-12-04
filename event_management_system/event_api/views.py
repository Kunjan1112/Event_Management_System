from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'user_app/index.html')

def event(request):
    return render(request, 'user_app/event.html')

def about(request):
    return render(request, 'user_app/about.html')

def contact(request):
    return render(request, 'user_app/contact.html')