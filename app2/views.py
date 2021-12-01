from django.shortcuts import render

# Create your views here.
def funMaster(request):
    return render(request,'adhome.html')
def fundoctor(request):
    return render(request,'doctors.html')
def funnurse(request):
    return render(request,'nurse.html')
def funappoinment(request):
    return render(request,'appoinment.html')
