
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
path('addashboard',views.funMaster,name='addashboard'),
path('doctors',views.fundoctor,name='doctors'),
path('nurse',views.funnurse,name='nurse'),
path('appoinment',views.funappoinment,name='appoinment'),
path('viewappoinments',views.funviewappoinments,name='viewappoinments'),
path('adminlogin',views.funadminlogin,name='adminlogin'),
path('canceledappoinment',views.funcanceledappoinment,name='canceledappoinment'),
]

