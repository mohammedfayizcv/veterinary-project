from django.db import models 
from django.db.models.deletion import CASCADE



# Create your models here.

# staffTable

    
# # doctor department
class doctordepartment(models.Model):
    nameofdepartment=models.CharField(max_length=80)
    status=models.CharField(max_length=12,null=True)
    
    # staff category
class staffCategory(models.Model):
    categoryname=models.CharField(max_length=30)     
    
    
# staff table

class StaffTable(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phonenumber=models.BigIntegerField()
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=30)
    staffcategory=models.ForeignKey(staffCategory,on_delete=models.CASCADE)
    department=models.ForeignKey(doctordepartment,on_delete=models.CASCADE)
    age=models.CharField(max_length=10)
    startedDate=models.CharField(max_length=20)
    salary=models.CharField(max_length=30)
    status=models.CharField(max_length=10,null=True)
    
    # nurse table
class nurseTable(models.Model):
    firstname=models.CharField(max_length=50)
    lasttname=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    mail=models.EmailField()
    staffcategory=models.ForeignKey(staffCategory,on_delete=models.CASCADE)
    department=models.ForeignKey(doctordepartment,on_delete=models.CASCADE)
    age=models.TextField(max_length=20)
    experience=models.CharField(max_length=30)
    startdate=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    status=models.CharField(max_length=10,null=True)
    
#doctor adding

class doctorTable(models.Model):
     firstname=models.CharField(max_length=30)
     lastname=models.CharField(max_length=20)
     phonenumber=models.CharField(max_length=30)
     email=models.EmailField()
     age=models.CharField(max_length=10)
     department=models.ForeignKey(doctordepartment,on_delete=models.CASCADE)
     startdate=models.CharField(max_length=20)
     salary=models.CharField(max_length=20)
     experience=models.CharField(max_length=30,null=True)
     image=models.CharField(max_length=300,null=True)
     status=models.CharField(max_length=10,null=True)
     
    
    
    
class Doctor_time_table(models.Model):
    Dr_name=models.ForeignKey(doctorTable,on_delete=models.CASCADE)
    Department=models.ForeignKey(doctordepartment,on_delete=models.CASCADE)
    time=models.CharField(max_length=60,null=True)
    status=models.CharField(max_length=10,null=True)
     

# services
class Service_Table(models.Model):
   Image=models.CharField(max_length=300,null=True)
   ServiceName=models.CharField(max_length=300,null=True)
   ServicesDetails=models.CharField(max_length=300,null=True)