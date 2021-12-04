from django.shortcuts import render

# Create your views here.
def funMaster(request):
    return render(request,'addashboard.html')
def fundoctor(request):
    return render(request,'doctors.html')
def funnurse(request):
    return render(request,'nurse.html')
def funappoinment(request):
    return render(request,'appoinment.html')
def funviewappoinments(request):
    return render(request,'viewappoinments.html')
def funadminlogin(request):
    return render(request,'adminlogin.html')
def funcanceledappoinment(request):
    return render(request,'canceledappoinment.html')