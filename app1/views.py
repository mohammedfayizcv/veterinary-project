from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from app3.models import *
from . models import *
from app2.models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from random import randint


# Create your views here.
def fun(request):
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_time=Doctor_time_table.objects.all()
    service=Service_Table.objects.all()
    context = {'doctor': obj_addDoc,'time':obj_time,'services':service}
    return render(request, 'index.html', context)


def funmaster(request):
    service=Service_Table.objects.all()
    context={'services':service}
    return render(request, 'master.html',context)


def fnabout(request):
    obj_addDoc = doctorTable.objects.filter(status=1)
    context = {'doctor': obj_addDoc}
    return render(request, 'about.html', context)


def fnservices(request):
    obj_addDoc = doctorTable.objects.filter(status=1)
    services=Service_Table.objects.all()
    context = {'doctor': obj_addDoc,'services':services}
    return render(request, 'services.html', context)


def fnpetfood(request):
    obj_pri = fooddetails.objects.all()
    return render(request, 'petfood.html', {'foodshow': obj_pri})


def fnblog(request):
    obj_pri = blogitems.objects.all()
    feed_view=feedbackTable.objects.all()
    return render(request, 'blog.html', {'show': obj_pri,'feedback':feed_view})

# read more blog area


def funcReadMore(request, readid):
    readBlog = blogitems.objects.filter(id=readid).get(id=readid)
    context = {'readMore': readBlog}
    return render(request, 'blogReadmore.html', context)

# petos_id 


# appoinmentform

def funAppoinment(request):
    try:
        obj_DOc = doctorTable.objects.filter(status=1)
        context = {'doctor': obj_DOc,}
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            date = request.POST['date']
            doctor = doctorTable.objects.get(id=request.POST['doctor'])
            pet = request.POST['pet']
            petname = request.POST['petname']
            petbreed = request.POST['petbreed']
            petdisease = request.POST['petdisease']
            petsex = request.POST['petsex']
            petage = request.POST['petage']
            petweight = request.POST['petweight']
            print(name, email, address, date, doctor, pet,
                  petname, petdisease, petsex, petage, petweight)
            obj_Dsave = appoinmenttable(name=name, email=email, address=address, date=date, doctor=doctor, pet=pet,
                                        petname=petname, petdisease=petdisease, petsex=petsex, petage=petage, petweight=petweight, petbreed=petbreed, status=1)
            obj_Dsave.save()
            send_mail(
               'Appointment is Registered',
                "This Appointment is registered,  "+name+"  We will inform you shortly via the next email to confirm your Token Number and Appoinment Time.",
                'fayizcv1@gmail.com',   
                [email],
                fail_silently=False,
            )
            obj_get = appoinmenttable.objects.get(
                name=name, email=email, petname=petname)
            request.session['usersess'] = obj_get.id
            print('id', obj_get.id)
            return redirect('getappoinment',context)
        # else:
        #     return render(request, 'index.html', context)
    except Exception as e:
        print(e)
    return render(request, 'index.html', context)




# viewappo
def funviewappoinment(request):
    print('step1')
    obj_sess = request.session['usersess']
    try:
        obj_apo = appoinmenttable.objects.get(id=obj_sess)
    except:
        obj_apo = ''
    context = {'appoin': obj_apo}
    return render(request, 'getappoinment.html', context)

# feedback view


def funfeed(request):
    try:
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            message = request.POST['message']
            print(firstname)
            print(lastname)
            print(message)
            obj_feedback = feedbackTable(
                firstname=firstname, lastname=lastname, email=email, phonumber=phonenumber, message=message)
            obj_feedback.save()
    except Exception as e:
        print(e)
    messages.info(request, "Your Feedback Sended")
    return redirect('index')


def funloginadmin(request):
    return render(request, 'login.html')


def funLogiall(request):
    email = request.POST['email']
    password = request.POST['password']
    if((email == 'admin@demo.com') and (password == "1234")):
        request.session['sess'] = '111'
        return redirect("/admin/addashboard")
    else:
        staff = StaffTable.objects.filter(
            email=email, password=password).exists()
        if staff:
            print("STep1")
            staffUser = StaffTable.objects.get(email=email, password=password)
            print("sTEP2")
            request.session['sTAFF'] = staffUser.id
            return redirect('staffdashboard')
        else:
            print("Invalid")
            messages.info(request, "Invalid Username Or Password ")
            return redirect('login')


# service appoinment

def funServiesAppoinment(request):
    try:
        service=Service_Table.objects.all()
        context = {'services':service}
        if request.method == 'POST':
            name = request.POST['yname']
            phonenumber = request.POST['phonenumber']
            email = request.POST['email']
            address = request.POST['address']
            date = request.POST['date']
            service = Service_Table.objects.get(id=request.POST['service'])
            pet = request.POST['pet']
            petname = request.POST['petname']
            petbreed = request.POST['petbreed']
            ambulance = request.POST['ambulance']
            petage = request.POST['petage']
            petweight = request.POST['petweight']
            print(name, email, address, date, pet,
                  petname, petage, petweight)
            obj_services_save = ServiceBookinTable(name=name,phonenumber=phonenumber, email=email, address=address, date=date, services=service, pet=pet,
                                        petname=petname,  ambulanceService=ambulance, petage=petage, petweight=petweight, petbreed=petbreed, status=1)
            obj_services_save.save()
            send_mail(
               'Service Booking Registerd',
                "This Booking is registered,  "+name+"  We will contact you shortly.",
                'fayizcv1@gmail.com',   
                [email],
                fail_silently=False,
            )
            return redirect('index',context)
    except Exception as e:
        print(e)
    return render(request, 'index.html')
