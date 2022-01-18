from os import name
from django.http.request import validate_host
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('staffdashboard',views.fundashboard,name='staffdashboard'),
    path('staffappoinment',views.funappoinment,name='staffappoinment'),
    path('staffviewappoinment',views.funstaffviewappoinment,name='staffviewappoinment'),
    path('staffcancelappo',views.funstaffcancelappo,name='staffcancelappo'),
    path('staffdoctor',views.funstaffdoctor,name='staffdoctor'),
    path('staffnurse',views.funstaffnurse,name='staffnurse'),
    path('staffpayment',views.funstaffpayment,name='staffpayment'),
    path('satfffeedbackview',views.funsatfffeedbackview,name='satfffeedbackview'),
    path('blogviews',views.funblogviews,name='blogviews'),
    path('editprofile/',views.funeditprofile,name='editprofile'),
    # edit profile save
    path('editedProfileSave/',views.funEditedProfile,name='editedProfileSave'),
    path('food/',views.funfood,name='food'),
    path('sideblog',views.funsideblog,name='sidelog'),  
    # appoinment
    path('stafappoinmet/',views.funnewappoin,name='stafappoinmet'),
    # delete appoinmet
    path('deleteAppoi/<appo_id>',views.funDeleteAppoinment,name='deleteAppoin'),
    # update appoinment
    path('editAppo/<appoId>',views.funEditAppoin,name='editAppo'),
    # saveEditAppoin
    path('editedAppopiSave/',views.funEditAppoSave,name='editedAppopiSave'),
    # add nurse 
    path('addnusreInStafs',views.funAddNurse,name='addnusreInStafs'),
    # delete nurse
    path('deletestaNurse/<denur_id>',views.funDeleteNUrse,name='deletestaNurse'),
    # update nurse
    path('updatestaNurse/<UpNurse>',views.funUpdateNurse,name='updatestaNurse'),
    # save updated nurse
    path('saveUpdatedNurse/',views.funsaveUpdateNurse,name='saveUpdatedNurse'),
    
    # delete staff
    path('removeStaff/<RemoSta>',views.funRemoveStaff,name='removeStaff'),
    # update staff details
    path('UpdateStaffId/<UpdSta_id>',views.funUpdateStaffDetails,name='UpdateStaffId'),
    # save updates
    path('saveUpdateStaffdetails/',views.funUpdateSaves,name='saveUpdateStaffdetails'),
    
    # logout staffuser
    path('logoutStaffUser/',views.funLogoutStaff,name='logoutStaffUser'),
    # delete blogs
    path('deleteBlogs/<blog_id>',views.fundeleteBlogs,name='deleteBlogs'),
    
    # update blogs
    path('UpdateBlogs/<UpdateBlo_id>',views.funUpdateBlog,name='UpdateBlogs'),
    
    # save Updated blogs
    path('saveUpdateBlogs/',views.funSaveUplodeBlog,name='saveUpdateBlogs'), 
    
    #token and time 
    path('tokenTime/<token_id>',views.funTokenTime,name='tokenTime'),
    
    path('savetoken/',views.funSaveToken,name='savetoken'),
    
    # servivce
    path('servicesView/',views.funServiceView,name='servicesView'),
    
    # remove service
    
    path('remove_service_book/<ReServ_id>',views.funRemoveService,name='remove_service_book'),
    # update service booking
    path('UpdateServiceBoo/upSer',views.funUpdateServBook,name='UpdateServiceBoo'),
    
  
    
]