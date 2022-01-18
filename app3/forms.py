from django.db.models import fields
from django.forms import ModelForm
from . models import *


class StaffFrom(ModelForm):
    class Meta:
        model=StaffTable
        fields='__all__'