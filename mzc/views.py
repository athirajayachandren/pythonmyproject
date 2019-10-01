from django.shortcuts import render
from django.http import HttpResponse
from .forms import FacultyForm

# Create your views here.

def indexpage(request):
    return render(request,'index.html')

def contactpage(request):
    return render(request,'contact.html')  

def homepage(request):
    return render(request,'home.html')     

def facultypage(request):
    if request.method=="POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully added")
    else:

        form=FacultyForm()
    return render(request,'faculty.html',{'form':form})
  