from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service
# Create your views here.

def index(request):
    context = {
        'services':Service.objects.all()
    }
    return render(request ,'pages/index.html' , context)

def about(request):
    return render(request ,'pages/about.html')

def issactrans(request):
    return render(request ,'pages/issactrans.html')
