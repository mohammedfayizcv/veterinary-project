from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fun(request):
   return render(request,'index.html')

def fnMaster(request):
   return render(request,'samplemaster.html')
def fnHome(request):
   return render(request,'home.html')