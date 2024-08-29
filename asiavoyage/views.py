from django.shortcuts import render
from django.http import HttpResponse

from .models import Tour

def index(request):
    tours = Tour.objects.all()
    
    context = {"tours": tours}
    
    return render(request, "tours/index.html", context)

def welcome(request):
    return HttpResponse("Welcome to Asia Voyage")

