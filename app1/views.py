from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fun(request):
   return render(request,'index.html')
def fnabout(request):
   return render(request,'about.html')
def fnservices(request):
   return render(request,'services.html')
def fnpetfood(request):
   return render(request,'petfood.html')
def fnblog(request):
   return render(request,'blog.html')
