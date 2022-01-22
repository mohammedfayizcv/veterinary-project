from contextvars import Token
import email
from unicodedata import name
from django.shortcuts import redirect, render
from app1.models import *
from app1.models import appoinmenttable, feedbackTable
from app2.models import *
from random import random
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from app3.forms import StaffFrom
from random import randint
from app3.models import TokenNumber, blogitems, fooddetails, sidebolg
from datetime import date
from django.core.mail import send_mail
from .decorators import staff_log 


# Create your views here.
@staff_log
def fundashboard(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_appoinment = appoinmenttable.objects.filter(status=1,date=date.today())
    obj_count = appoinmenttable.objects.filter(status=1,date=date.today()).count()
    obj_token=TokenNumber.objects.filter(date=date.today())
    obj_service=ServiceBookinTable.objects.filter(status=1,date=date.today())
    context={'doctor': obj_addDoc,'appoinment': obj_appoinment,'coun':obj_count,'token':obj_token,'servi_book':obj_service,'editPro':obj_staff}
    return render(request, 'staffdashboard.html',context)


# appoinmet
@staff_log
def funappoinment(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_appoinment = appoinmenttable.objects.filter(status=1,date=date.today())
    obj_count = appoinmenttable.objects.filter(status=1,date=date.today()).count()
    context = {'appoinment': obj_appoinment, 'doctor': obj_addDoc,'coun':obj_count,'editPro':obj_staff}
    return render(request, 'staffappoinment.html', context)

@staff_log
def funstaffviewappoinment(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_appoinment = appoinmenttable.objects.all()
    obj_addDoc = doctorTable.objects.all()
    context={'appoinment': obj_appoinment, 'doctor': obj_addDoc,'editPro':obj_staff}
    return render(request, 'staffviewappoinment.html',context)

@staff_log
def funstaffcancelappo(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_appoinment = appoinmenttable.objects.filter(status=0)
    context={'appoinment': obj_appoinment, 'doctor': obj_addDoc,'editPro':obj_staff}
    return render(request, 'staffcancelappo.html',context)

@staff_log
def funstaffdoctor(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_addDoc = doctorTable.objects.filter(status=1)
    return render(request, 'staffdoctor.html', {'doctor': obj_addDoc,'editPro':obj_staff})

@staff_log
def funstaffnurse(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_add = doctordepartment.objects.filter(status=1)
    obj_as = staffCategory.objects.all()
    obj_staffView = StaffTable.objects.filter(status=1)
    obj_ns = nurseTable.objects.filter(status=1)
    context = {'doc': obj_add, 'staffview': obj_staffView,
               'cate': obj_as, 'nur': obj_ns,'editPro':obj_staff}
    return render(request, 'staffnurse.html', context)

@staff_log
def funstaffpayment(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    return render(request, 'staffpayment.html',{'editPro':obj_staff})

@staff_log
def funsatfffeedbackview(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_mssg = feedbackTable.objects.all()
    return render(request, 'satfffeedbackview.html', {'feedback': obj_mssg,'editPro':obj_staff})


# blogviews
def funblogviews(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    try:
        if request.method == "POST":
            file = request.FILES['photos']
            petname = request.POST['petname']
            name = request.POST['name']
            date = request.POST['date']
            heading = request.POST['heading']
            textarea = request.POST['textarea']
            file_name = str(random())+file.name
            print(file_name)
            obj_store = FileSystemStorage()
            obj_store.save(file_name, file)
            obj = blogitems(photo=file_name, petname=petname, name=name,
                            date=date, heading=heading, textarea=textarea,status=1)
            obj.save()
    except Exception as e:
        print(e)
    obj_pri = blogitems.objects.filter(status=1)
    return render(request, 'blogviews.html', {'show': obj_pri,'editPro':obj_staff})


# # sideblog
def funsideblog(request):
    # try:
        if request.method == "POST":
            print('hello123')
            file = request.FILES['image']
            heading = request.POST['heading']
            textarea = request.POST['textarea']
            file_name = str(random())+file.name
            print(file_name)
            obj_Str = FileSystemStorage()
            obj_Str.save(file_name, file)
            obj_1 = sidebolg(photo=file_name, heading=heading,
                             textarea=textarea,status=1)
            obj_1.save()
            messages.info(request,"Uploaded Successfully")
    # except Exception as e:
    #     print(e)
        obj_show = sidebolg.objects.all()
        return redirect('blogviews', {'sho': obj_show})

@staff_log
def funeditprofile(request):
    Edst=request.session['sTAFF']
    userSta=StaffTable.objects.get(id=Edst)
    context={'editPro':userSta}
    return render(request, 'editprofile.html',context)

# save updates
def funEditedProfile(request):
    if request.method=='POST':
        stafftbid=request.POST['stafftbid']
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phonenumber = request.POST['phonnumber']
        print('ijaz')
        password = request.POST['password']
        StaffTable.objects.filter(id=stafftbid).update(name=name, lastname=lastname, phonenumber=phonenumber, email=email,
                                         password=password,status=1)
        messages.info(request,"update Successfully")
        return redirect('editprofile')
        
    


def funfood(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    try:
        if request.method == "POST":
            file = request.FILES['photo']
            protien = request.POST['protien']
            pet = request.POST['pet']
            heading = request.POST['heading']
            print(file)
            file_name = str(random())+file.name
            print(file_name)
            obj_store = FileSystemStorage()
            obj_store.save(file_name, file)
            obj_food = fooddetails(
                photo=file_name, protiename=protien, pet=pet, protiendetails=heading,status=1)
            obj_food.save()
    except Exception as e:
        print(e)
    obj_pri = fooddetails.objects.all()
    return render(request, 'food.html', {'foodshow': obj_pri,'editPro':obj_staff})

# delete appoinment
def funDeleteAppoinment(request, appo_id):
    obj_dele_appo = appoinmenttable.objects.filter(id=appo_id)
    obj_dele_appo.update(status=0)
    messages.info(request,'Deleted Appoinment')
    return redirect('staffappoinment')


# edit Appoinmet
@staff_log
def funEditAppoin(request,appoId):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_addDoc = doctorTable.objects.filter(status=1)
    obj_appoinment=appoinmenttable.objects.get(id=appoId)
    context={'Doctor':obj_addDoc,'Appoi':obj_appoinment,'editPro':obj_staff}
    return render(request,'editappoinment.html',context)

# edit appo save
def funEditAppoSave(request):
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
        AppoTbid=request.POST['AppoTbid']
        print(name, email, address, date, doctor, pet,
                petname, petdisease, petsex, petage, petweight)
        appoinmenttable.objects.filter(id=AppoTbid).update(name=name, email=email, address=address, date=date, doctor=doctor, pet=pet,
                                    petname=petname, petdisease=petdisease, petsex=petsex, petage=petage, petweight=petweight, petbreed=petbreed,status=1)
    messages.info(request,"Appoinment Updated Successflly")
    return redirect('staffappoinment')

# take new apppoinment

def funnewappoin(request):
    try:
        obj_DOc = doctorTable.objects.filter(status=1)
        context = {'doctor': obj_DOc}
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
                                        petname=petname, petdisease=petdisease, petsex=petsex, petage=petage, petweight=petweight, petbreed=petbreed,status=1)
            obj_Dsave.save()
            send_mail(
               'Appointment is Registered',
                "This Appointment is registered,  "+name+"  We will inform you shortly via the next email to confirm your Token Number and Appoinment Time.",
                'fayizcv1@gmail.com',   
                [email],
                fail_silently=False,
            )
            messages.info(request,'Successfully taken appoinment')
            return redirect( 'staffappoinment' )
    except Exception as e:
        print(e)
    return render(request, 'staffappoinment.html', context)


# add nurse in staff


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
                return redirect('staffnurse')
            else:
                context = {'mgs1': 'email already exists',
                           'doc': obj_add, 'cate': obj_as}
                return render(request, 'staffnurse.html', context)
        else:
            return render(request, 'staffnurse.html', context)
    except Exception as e:
        print(e)
    return render(request, 'staffnurse.html', context)

# delete nurse
def funDeleteNUrse(request,denur_id):
    obj_nur_dele=nurseTable.objects.filter(id = denur_id)
    obj_nur_dele.update(status = 0)
    messages.info(request, 'Nurse Removed')
    return redirect('staffnurse')

# update staff
@staff_log
def funUpdateNurse(request,UpNurse):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_add = doctordepartment.objects.filter(status=1)
    obj_as = staffCategory.objects.all()
    obj_Nurse=nurseTable.objects.get(id=UpNurse)
    context= context = {'doc': obj_add, 'cate': obj_as,'edit':obj_Nurse,'editPro':obj_staff}
    return render(request,'staffNurseUpdate.html',context)

# saveUpdate nurse
def funsaveUpdateNurse(request):
     if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        nurseTbid=request.POST['nurseTbid']
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
        messages.info(request,"Updated Successfully")
        return redirect("staffnurse")
    
# delete staff
def funRemoveStaff(request,RemoSta):
    obje_stf_del=StaffTable.objects.filter(id = RemoSta)
    obje_stf_del.update(status = 0)
    messages.info(request, 'Removed Staff')
    return redirect('staffnurse')

# Update staff 
def funUpdateStaffDetails(request,UpdSta_id):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    obj_as = staffCategory.objects.all()
    obj_add = doctordepartment.objects.filter(status=1)
    obj_sta = StaffTable.objects.get(id=UpdSta_id)
    context={'stafo': obj_sta, 'cate': obj_as, 'doc': obj_add,'editPro':obj_staff}
    return render(request, 'updateStaffdetails.html', context)

# save updated staff details

def funUpdateSaves(request):
    if request.method=='POST':
        stafftbid=request.POST['stafftbid']
        name = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['staemail']
        phonenumber = request.POST['phonenumber']
        print('ijaz')
        password = request.POST['password']
        category = staffCategory.objects.get(id=request.POST['category'])
        department = doctordepartment.objects.get(id=request.POST['department'])
        age = request.POST['age']
        startdate = request.POST['date']
        salary = request.POST['salary']
        
        StaffTable.objects.filter(id=stafftbid).update(name=name, lastname=lastname, phonenumber=phonenumber, email=email,
                                        department=department, staffcategory=category, password=password, age=age, startedDate=startdate, salary=salary,status=1)
        messages.info(request,"update Successfully")
        return redirect('staffnurse')
    
    
# staff user logout
@staff_log
def funLogoutStaff(request):
    del request.session['sTAFF']
    return render(request, 'login.html')

# delete blogs
def fundeleteBlogs(request,blog_id):
    deleBlog=blogitems.objects.filter(id=blog_id)
    deleBlog.update(status=0)
    messages.info(request,"Blog deleted")
    return redirect('blogviews')

# update blogs
@staff_log
def funUpdateBlog(request,UpdateBlo_id):
    obj_blog=blogitems.objects.get(id=UpdateBlo_id)
    return render(request,'staffUpdateBlog.html',{'UpBlog':obj_blog})


# save blogs 
def funSaveUplodeBlog(request):
     if request.method == "POST":
            petname = request.POST['petname']
            name = request.POST['name']
            date = request.POST['date']
            heading = request.POST['heading']
            textarea = request.POST['textarea']
            Blogid=request.POST['Blogid']
            blogitems.objects.filter(id=Blogid).update(petname=petname, name=name,
                            date=date, heading=heading, textarea=textarea,status=1)
            messages.info(request,'Updated Successfully')
            return redirect('blogviews')



# token and Time
@staff_log
def funTokenTime(request,token_id):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    print(token_id)    
    obj_appoinment=appoinmenttable.objects.get(id=token_id)
    obj_time=Doctor_time_table.objects.filter(status=1)
    obj_doc=doctorTable.objects.get(id=obj_appoinment.doctor_id)
    context={'Appoi':obj_appoinment,'doct':obj_doc,'time':obj_time,'editPro':obj_staff}
    return render(request,'token_time.html',context)
    
# token number genrate
# token= randint(1,20)

# Save token
def funSaveToken(request):
    if request.method=='POST':
        time=Doctor_time_table.objects.get(id=request.POST['time'])
        name=request.POST['name']
        email=request.POST['email']
        doctor=request.POST['doctor']
        token_number=request.POST['token']     
        date=request.POST['date'] 
        print(token_number)
        obj_to_save=TokenNumber(token_id=token_number,name=name,email=email,doctor=doctor,time=time,date=date)
        obj_to_save.save()
        messages.info(request,"Successflly")
        send_mail(
            'Your Token Number and Time',
                "Dear,  "+name+"  your Token Number is "+token_number+" Appoinment with "+doctor+" is scheduled for "+date+","+time.time+" Please visit hospital 30 mins before scheduled time  PETOS vetCARE",
                'fayizcv1@gmail.com',   
                [email],
                fail_silently=False,
            )
        
        return redirect('staffdashboard')  


# srevice view
@staff_log
def funServiceView(request):
    Edst=request.session['sTAFF']
    obj_staff=StaffTable.objects.get(id=Edst)
    service=ServiceBookinTable.objects.filter(status=1)
    context={'show_serv':service,'editPro':obj_staff}
    return render(request,'serviceview.html',context)

# remove service booking

def funRemoveService(request,ReServ_id):
    remove_servi=ServiceBookinTable.objects.filter(id=ReServ_id)
    remove_servi.update(status=0)
    messages.info(request,"Service Booking Removed")
    return redirect('servicesView')


def funUpdateServBook(request):
    pass