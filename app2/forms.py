from django.db.models import fields
from django.forms import ModelForm
from . models import *
from django import forms


class StaffFrom(ModelForm):
    class Meta:
        model=StaffTable
        fields='__all__'
        
# class timeform(ModelForm):
#     class Meta:
#         model=Doctor_time_table
#         fields='__all__'
        
    
            