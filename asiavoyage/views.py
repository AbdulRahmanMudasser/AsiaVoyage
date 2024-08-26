from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Asia Voyage")

def welcome(request):
    return HttpResponse("Welcome to Asia Voyage")

