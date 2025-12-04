from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name(request):
    return HttpResponse("Hello World!")

def index_view(request):
    return render(request, 'user_app/index.html')

def event_view(request):
    return render(request, 'user_app/event.html')

def about_view(request):
    return render(request, 'user_app/about.html')

def contact_view(request):
    return render(request, 'user_app/contact.html')