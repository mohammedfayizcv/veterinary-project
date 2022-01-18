from django.db import models

from app2.models import Service_Table, doctorTable,Doctor_time_table 

# Create your models here.


class appoinmenttable(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    date = models.CharField(max_length=90)
    doctor = models.ForeignKey(doctorTable, on_delete=models.CASCADE)
    pet = models.CharField(max_length=34)
    petname = models.CharField(max_length=34, null=True)
    petbreed = models.CharField(max_length=30)
    petdisease = models.CharField(max_length=50)
    petsex = models.CharField(max_length=20)
    petage = models.CharField(max_length=30)
    petweight = models.CharField(max_length=30)
    status = models.CharField(max_length=10, null=True)
  



# feedback
class feedbackTable(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phonumber = models.BigIntegerField()
    message = models.TextField()



# service table
class ServiceBookinTable(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    date = models.CharField(max_length=90)
    services = models.ForeignKey(Service_Table, on_delete=models.CASCADE)
    pet = models.CharField(max_length=34)
    petname = models.CharField(max_length=34, null=True)
    petbreed = models.CharField(max_length=30)
    ambulanceService = models.CharField(max_length=20)
    petage = models.CharField(max_length=30)
    petweight = models.CharField(max_length=30)
    status = models.CharField(max_length=10, null=True)


