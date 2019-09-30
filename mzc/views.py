from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexpage(request):
    return render(request,'index.html')

def contactpage(request):
    return render(request,'contact.html')  

def homepage(request):
    return render(request,'home.html')     