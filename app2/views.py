from random import random
from typing import ContextManager
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import redirect, render
from app1.models import *
from app2.models import *
from app3.models import *
from . models import Doctor_time_table
from datetime import date
from .decorators import admin_log
# Create your views here.

@admin_log
def funMaster(request):
    obj_appoinment = appoinmenttable.objects.all().count()
    obj_pet = appoinmenttable.objects.filter(status=1).count()
    obj_todaappo = appoinmenttable.objects.filter(status=1,date=date.today())
    obj_count_service=ServiceBookinTable.objects.all().count
    service=ServiceBookinTable.objects.filter(status=1,date=date.today())
    print('number of ammpoinment', obj_appoinment)
    context = {'appoinment': obj_appoinment, 'pet_patient': obj_pet,'today_app':obj_todaappo,'countservice':obj_count_service,'Bookservice':service}
    return render(request, 'addashboard.html', context)

@admin_log
def fundoctor(request):
    obj_add = doctordepartment.objects.filter(status=1)
    obj_addDoc = doctorTable.objects.filter(status=1)
    print('helooo')
    context = {'doc': obj_add, 'doctor': obj_addDoc}
    return render(request, 'doctors.html', context)

# #   add staff

@admin_log
def funnurse(request):
    obj_staffView = StaffTable.objects.filter(status=1)
    print("Aloooooo2345678")
    obj_add = doctordepartment.objects.filter(status=1)
    obj_as = staffCategory.objects.all()
    obj_ns = nurseTable.objects.filter(status=1)
    context = {'doc': obj_add, 'staffview': obj_staffView,
               'cate': obj_as, 'nur': obj_ns}
    return render(request, 'nurse.html', context)


# appoinment
@admin_log
def funappoinment(request):
    obj_appoinment = appoinmenttable.objects.filter(status=1)
    return render(request, 'appoinment.html', {'appoinment': obj_appoinment})

@admin_log
def funviewappoinments(request):
    obj_appoinment = appoinmenttable.objects.all()
    obj_addDoc = doctorTable.objects.all()
    return render(request, 'viewappoinments.html', {'appoinment': obj_appoinment, 'doctor': obj_addDoc})

@admin_log
def funcanceledappoinment(request):
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_appoinment = appoinmenttable.objects.filter(status=0)
    context = {'appoinment': obj_appoinment, 'doctor': obj_addDoc}
    return render(request, 'canceledappoinment.html', context)

@admin_log
def funnursedepartment(request):
    obj_add = doctordepartment.objects.filter(status=1)
    return render(request, 'nursedepartment.html', {'doc': obj_add})


def funpayment(request):
    return render(request, 'payment.html')


# feedbackvipyewss
@admin_log
def funfeedbackview(request):
    obj_mssg = feedbackTable.objects.all()
    return render(request, 'feedbackview.html', {'feedback': obj_mssg})


# staff adding
def funStaff(request):
    try:
        print("hwloo35")
        obj_add = doctordepartment.objects.filter(status=1)
        obj_as = staffCategory.objects.all()
        context = {'doc': obj_add, 'cate': obj_as}
        if request.method == "POST":
            email = request.POST['email']
            obj_1 = StaffTable.objects.filter(email=email).exists()
            if(obj_1 == False):
                name = request.POST['firstname']
                lastname = request.POST['lastname']
                phonenumber = request.POST['phonenumber']
                password = request.POST['password']
                category = staffCategory.objects.get(
                    id=request.POST['category'])
                department = doctordepartment.objects.get(
                    id=request.POST['department'])
                age = request.POST['age']
                startdate = request.POST['date']
                salary = request.POST['salary']
                print(name)
                print(email, category, department, startdate, salary, password)
                obj_save = StaffTable(name=name, lastname=lastname, phonenumber=phonenumber, email=email,
                                      department=department, staffcategory=category, password=password, age=age, startedDate=startdate, salary=salary, status=1)
                obj_save.save()
                context = {'mgs1': 'Saved Successfully',
                           'doc': obj_add, 'cate': obj_as}
                return render(request, 'nurse.html', context)
            else:
                context = {'mgs1': 'email already exists',
                           'doc': obj_add, 'cate': obj_as}
                return render(request, 'nurse.html', context)
        else:
            return render(request, 'nurse.html',)

    except Exception as e:
        print(e)
    return render(request, 'nurse.html', context)

# department

@admin_log
def funcdepart(request):
    try:
        print("heloo")
        obj_add = doctordepartment.objects.all
        context = {'doc': obj_add, }
        if request.method == 'POST':
            department = request.POST['department']
            obj_dep = doctordepartment(nameofdepartment=department, status=1)
            print(department)
            obj_dep.save()
            obj_add = doctordepartment.objects.all()
            messages.info(request, 'Department Added')
            return redirect('nursedepartment')
        else:
            return render(request, 'nursedepartment.html', context)
    except Exception as e:
        print(e)
    return render(request, 'nursedepartment.html', context)


def funlogout(request):
    del request.session['sess']
    return render(request, 'login.html')

@admin_log
def funcategory(request):
    try:
        category = request.POST['category']
        obj_dep = staffCategory(categoryname=category)
        print(category)
        obj_dep.save()
    except Exception as e:
        print(e)    
    obj_cate = staffCategory.objects.all()
    return render(request, 'category.html', {'category': obj_cate})


# add nurse

def funAddNurse(request):
    try:
        obj_ns = nurseTable.objects.filter(status=1)
        obj_add = doctordepartment.objects.filter(status=1)
        obj_as = staffCategory.objects.all()
        context = {'doc': obj_add, 'cate': obj_as, 'nur': obj_ns}
        if request.method == 'POST':
            email = request.POST['email']
            obj_nurse = nurseTable.objects.filter(mail=email).exists()
            if(obj_nurse == False):
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                phonenumber = request.POST['phone']
                category = staffCategory.objects.get(
                    id=request.POST['category'])
                department = doctordepartment.objects.get(
                    id=request.POST['department'])
                age = request.POST['age']
                experience = request.POST['experience']
                startdate = request.POST['date']
                salary = request.POST['salary']
                print(firstname, lastname, category)
                obj_nSave = nurseTable(firstname=firstname, lasttname=lastname, phonenumber=phonenumber, staffcategory=category,
                                       department=department, mail=email, age=age, experience=experience, startdate=startdate, salary=salary, status=1)
                obj_nSave.save()
                context = {'mgs1': 'Saved Successfully',
                           'doc': obj_add, 'cate': obj_as, }
                return redirect('nurse')
            else:
                context = {'mgs1': 'email already exists',
                           'doc': obj_add, 'cate': obj_as}
                return render(request, 'nurse.html', context)
        else:
            return render(request, 'nurse.html', context)
    except Exception as e:
        print(e)
    return render(request, 'nurse.html', context)


# doctor adding
@admin_log
def funAddDoctors(request):
    try:
        obj_addDoc = doctorTable.objects.all()
        obj_add = doctordepartment.objects.filter(status=1)
        context = {'docto': obj_add, 'doctor': obj_addDoc, }
        if request.method == 'POST':
            email = request.POST['email']
            obj_doct = doctorTable.objects.filter(email=email).exists()
            if(obj_doct == False):
                fstname = request.POST['firstname']
                lsname = request.POST['lastname']
                phonenumber = request.POST['phone']
                image = request.FILES['image']
                file_name = str(random())+image.name
                obj_sot = FileSystemStorage()
                obj_sot.save(file_name, image)
                age = request.POST['age']
                department = doctordepartment.objects.get(
                    id=request.POST['department'])
                startdate = request.POST['date']
                salary = request.POST['salary']
                experience = request.POST['experience']
                print(lsname, phonenumber, email, department)
                obj_dsave = doctorTable(image=file_name, firstname=fstname, lastname=lsname, phonenumber=phonenumber, email=email,
                                        age=age, department=department, salary=salary, startdate=startdate, experience=experience, status=1)
                obj_dsave.save()
                print(fstname, department, salary)
                context = {'mssgg': 'Saved Successfully', 'doc': obj_add}
                return redirect('doctors', context)
            else:
                context = {'mssgg': 'emial is already exists', 'doc': obj_add}
                return render(request, 'doctors.html', context)
        else:
            return render(request, 'doctors.html', context)
    except Exception as e:
        print(e)
    return render(request, 'doctors.html', context)


# update staff
@admin_log
def funStaffUpdate(request, sid):
    print(sid)
    print('helloo')
    obj_as = staffCategory.objects.all()
    obj_add = doctordepartment.objects.filter(status=1)
    obj_sta = StaffTable.objects.get(id=sid)
    context = {'stafo': obj_sta, 'cate': obj_as, 'doc': obj_add, }
    return render(request, 'updatestaff.html', context)

# save updates


def funupdatesave(request):
    if request.method == 'POST':
        stafftbid = request.POST['stafftbid']
        name = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['staemail']
        phonenumber = request.POST['phonenumber']
        print('ijaz')
        password = request.POST['password']
        category = staffCategory.objects.get(id=request.POST['category'])
        department = doctordepartment.objects.get(
            id=request.POST['department'])
        age = request.POST['age']
        startdate = request.POST['date']
        salary = request.POST['salary']

        StaffTable.objects.filter(id=stafftbid).update(name=name, lastname=lastname, phonenumber=phonenumber, email=email,
                                                       department=department, staffcategory=category, password=password, age=age, startedDate=startdate, salary=salary, status=1)
        messages.info(request, "update Successfully")
        return redirect('nurse')


# update nurse
@admin_log
def funUpdateNrse(request, nurid):
    obj_add = doctordepartment.objects.filter(status=1)
    obj_as = staffCategory.objects.all()
    obj_Nurse = nurseTable.objects.get(id=nurid)
    context = context = {'doc': obj_add, 'cate': obj_as, 'edit': obj_Nurse}
    return render(request, 'Updatenurse.html', context)


# nurse update save
def funUpdateSave(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        nurseTbid = request.POST['nurseTbid']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phone']
        category = staffCategory.objects.get(
            id=request.POST['category'])
        department = doctordepartment.objects.get(
            id=request.POST['department'])
        age = request.POST['age']
        experience = request.POST['experience']
        startdate = request.POST['date']
        salary = request.POST['salary']
        print(firstname, lastname, category)
        nurseTable.objects.filter(id=nurseTbid).update(firstname=firstname, lasttname=lastname, phonenumber=phonenumber, staffcategory=category,
                                                       department=department, mail=email, age=age, experience=experience, startdate=startdate, salary=salary, status=1)
        messages.info(request, "Updated Successfully")
        return redirect("nurse")
# deletedepartment


def funDepartDelete(request, dep):
    obj_del = doctordepartment.objects.filter(id=dep)
    obj_del.update(status=0)
    messages.info(request, 'Department Removed')
    return redirect('nursedepartment')

# updateDoctor details
@admin_log
def funUpdateDoctor(request, doctor_id):
    obj_add = doctordepartment.objects.filter(status=1)
    obj_addDoc = doctorTable.objects.get(id=doctor_id)
    context = {'doc': obj_add, 'doctor': obj_addDoc}
    return render(request, 'doctorupdate.html', context)

# save Doctor Update
def funUpdateSave(request):
    if request.method == 'POST':
        email = request.POST['email']
        doctorTbId = request.POST['doctorTbId']
        fstname = request.POST['firstname']
        lsname = request.POST['lastname']
        phonenumber = request.POST['phone']
        age = request.POST['age']
        department = doctordepartment.objects.get(
            id=request.POST['department'])
        startdate = request.POST['date']
        salary = request.POST['salary']
        experience = request.POST['experience']
        print(lsname, phonenumber, email, department)
        doctorTable.objects.filter(id=doctorTbId).update(firstname=fstname, lastname=lsname, phonenumber=phonenumber, email=email,
                                                         age=age, department=department, salary=salary, startdate=startdate, experience=experience, status=1)
        messages.info(request, 'Updated Successfully')
        return redirect("doctors")


# deletedoctor
def funDoctDelete(doc):
    obj_dodele = doctorTable.objects.filter(id=doc)
    obj_dodele.update(status=0)
    return redirect('doctors')
# delete nursr


def funNurseDelete(request, nurse):
    obj_nur_dele = nurseTable.objects.filter(id=nurse)
    obj_nur_dele.update(status=0)
    messages.info(request, 'Nurse Removed')
    return redirect('nurse')

# delete staff


def deleteStaff(request, staff_id):
    obje_stf_del = StaffTable.objects.filter(id=staff_id)
    obje_stf_del.update(status=0)
    messages.info(request, 'Removed Staff')
    return redirect('nurse')


# time scheduling
@admin_log
def funTime(request):
    obj_time= Doctor_time_table.objects.filter(status=1)
    obj_add = doctordepartment.objects.filter(status=1)
    obj_addDoc = doctorTable.objects.filter(status=1)
    context = {'Depart': obj_add, 'Docto': obj_addDoc,'time':obj_time}
    return render(request, 'doctortime.html', context)


# scheduling
@admin_log
def funTimeSchedu(request):
    try:
        obj_time= Doctor_time_table.objects.all()
        obj_add = doctordepartment.objects.filter(status=1)
        obj_addDoc = doctorTable.objects.filter(status=1)
        context = {'Depart': obj_add, 'Docto': obj_addDoc,'time':obj_time}
        if request.method == "POST":
            name_of_doctor = doctorTable.objects.get(
                id=request.POST['doctorname'])
            department = doctordepartment.objects.get(
                id=request.POST['department'])
            start_time=request.POST['starttime']
            print(name_of_doctor,start_time)
            obj_time_save=Doctor_time_table(Dr_name=name_of_doctor,Department=department,time=start_time,status=1)
            obj_time_save.save()
            return redirect('doctortime')
    except:
     return render(request,'doctortime.html',context)
 
#  edit time schedule
@admin_log
def funEditTime(request,time_id):
    obj_add = doctordepartment.objects.filter(status=1)
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_time= Doctor_time_table.objects.get(id=time_id)
    context={'Depart': obj_add, 'Docto': obj_addDoc,'time':obj_time}
    return render(request,'editTime.html',context)

# save edits
def funSaveTime(request):
    if request.method=="POST":
        name_of_doctor = doctorTable.objects.get(
                    id=request.POST['doctorname'])
        department = doctordepartment.objects.get(
            id=request.POST['department'])
        start_time=request.POST['starttime']
        timeid=request.POST['timeid']
        print(name_of_doctor,start_time)
        Doctor_time_table.objects.filter(id=timeid).update(Dr_name=name_of_doctor,Department=department,time=start_time,status=1)
        messages.info(request,'Update Save Successfully')
        return redirect('doct_time')

#remove time schedule

def funTimeDelete(request,del_it):
     obj_ti_de=Doctor_time_table.objects.filter(id=del_it)
     obj_ti_de.update(status=0)
     messages.info('Removed')
     return redirect('doct_time') 
 
#  services
@admin_log
def funServices(request):
    obj_show_detail=Service_Table.objects.all()
    return render(request,'addservices.html',{'show_serv':obj_show_detail})
    

# new services

def funNewServices(request):
    try:
        servicename = request.POST['servicename']
        servicedetails = request.POST['servicedetails']
        image = request.FILES['image']
        file_name = str(random())+image.name
        obj_sot = FileSystemStorage()
        obj_sot.save(file_name, image) 
        print(image,servicename)
        obj_service=Service_Table(Image=file_name,ServiceName=servicename,ServicesDetails=servicedetails)
        obj_service.save()
        print(image,servicename)
        messages.info(request,'New Service Created')
    except Exception as e:print(e)
    return redirect('addservice')

# services booking 

@admin_log
def funserviceBook(request):
    view_serv_book=ServiceBookinTable.objects.filter(status=1)
    
    return render(request,'serviceBookinDetail.html',{'show_booking':view_serv_book})