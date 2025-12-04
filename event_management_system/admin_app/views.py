from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name_view(request):
    return HttpResponse("Admin App: Hello World!")

def index_view(request):
    return render(request, 'admin_app/index.html')

def event_view(request):
    return render(request, 'admin_app/event.html')