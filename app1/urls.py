
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
path ('',views.fun,name=''),
path('master/',views.fnMaster,name='master'),
path('home/',views.fnHome,name='home')
]
