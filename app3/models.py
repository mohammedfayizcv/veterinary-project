from time import time
from django.db import models
from django.db.models.aggregates import Min
from app1.models import appoinmenttable
from app2.models import *
from django.db.models.deletion import CASCADE
# Create your models here.
# blog 
class blogitems(models.Model):
    photo=models.CharField(max_length=400)
    petname=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    heading=models.CharField(max_length=30)
    textarea=models.CharField(max_length=800)
    status=models.CharField(max_length=10,null=True)
    
class fooddetails(models.Model):
    photo=models.CharField(max_length=400)
    protiename=models.CharField(max_length=30)
    pet=models.CharField(max_length=30)
    protiendetails=models.CharField(max_length=200)
    status=models.CharField(max_length=10,null=True)

class sidebolg(models.Model):
    photo=models.CharField(max_length=200)
    heading=models.CharField(max_length=20)
    textarea=models.TextField()
    status=models.CharField(max_length=10,null=True)
    

# token number

class TokenNumber(models.Model):
    token_id=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    time=models.ForeignKey(Doctor_time_table,on_delete=models.CASCADE)
    doctor=models.CharField(max_length=30)
    date=models.CharField(max_length=50,null=True)
    