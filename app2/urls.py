
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
path('adhome',views.funMaster,name='adhome'),
path('doctors',views.fundoctor,name='doctors'),
path('nurse',views.funnurse,name='nurse'),
path('appoinment',views.funappoinment,name='appoinment'),

]

