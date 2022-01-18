
from django.urls import path
from django.urls.conf import include

from .import views

from app2 . models import *

urlpatterns = [
path ('',views.fun,name='index'),
path('about/',views.fnabout,name='about'),
path('services/',views.fnservices,name='services'),
path('petfood/',views.fnpetfood,name='petfood'),
path('blog/',views.fnblog,name='blog'),
path('getappoinment/',views.funAppoinment,name='getappoinment'),    
path('appoinmentview/',views.funviewappoinment,name='appoinmentview'),
path('feedback',views.funfeed,name='feedbackview'),
path('login/',views.funloginadmin,name='login'),
path('loginall/',views.funLogiall,name='loginall'),
path('master',views.funmaster,name='master'),
# read more
path('readMore/<readid>',views.funcReadMore,name='readMore'),
# service appoinment
path('serviceAppoinment/',views.funServiesAppoinment,name='serviceAppoinment'),


]
