
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
path ('index',views.fun,name='index'),
path('about',views.fnabout,name='about'),
path('services',views.fnservices,name='services'),
path('petfood',views.fnpetfood,name='petfood'),
path('blog',views.fnblog,name='blog')
]
