
from os import name
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
path('addashboard/',views.funMaster,name='addashboard'),
path('doctors',views.fundoctor,name='doctors'),

path('nurse',views.funnurse,name='nurse'),

path('appoinment',views.funappoinment,name='appoinment'),
path('viewappoinments',views.funviewappoinments,name='viewappoinments'),
path('canceledappoinment',views.funcanceledappoinment,name='canceledappoinment'),
path('nursedepartment/',views.funnursedepartment,name='nursedepartment'),
path('payment',views.funpayment,name='payment'),
path('feedbackview',views.funfeedbackview,name='feedbackview'),
path('staff',views.funStaff,name='staff'),
path('adlogout/',views.funlogout,name='adlogout'),
path('newdepart/',views.funcdepart,name='newdepart'),
path('category/',views.funcategory,name='category'),
path('addnurse',views.funAddNurse,name='addnurse'),
path('doctor',views.funAddDoctors,name='doctor'),

# deletedep
path('deleteDepart/<dep>',views.funDepartDelete,name='deleteDepart'),

# delededoc
path('deleDoct/<doc>',views.funDoctDelete,name='deleDoct'),

# delete nurse
path('deleNurse/<nurse>',views.funNurseDelete,name='deleteNurse'),

# delete staff
path('deleteStaff/<staff_id>',views.deleteStaff,name='deletStaff'),

# updating staff
path('updatestaff/<sid>',views.funStaffUpdate,name='updateStaff'),

# updatesave
path('updatesave/',views.funupdatesave,name='updatesave'),

# nurseUpdate
path('updateNurse/<nurid>',views.funUpdateNrse,name='updateNurse'),

# nurse Update save
path('updatenursesave/',views.funUpdateSave,name='updatenursesave'),

# update doctor
path('updateDoctor/<doctor_id>',views.funUpdateDoctor,name='updateDoctor'),

# updatesavedoctor
path('updateDoctorSave/',views.funUpdateSave,name='updateDoctorSave'),

# tmie scheduling
path('doct_time/',views.funTime,name='doct_time'),

# scheduling
path('schedule/',views.funTimeSchedu,name='schedule'),

# edit time
path('edit_time/<time_id>',views.funEditTime,name='edit_time'), 
# save edits
path('savetimeedit/',views.funSaveTime,name='savetimeedit'),

# remove time 
path('deletetime/<del_it>',views.funTimeDelete,name='deletetime'),

# services
path('addservice/',views.funServices,name='addservice'),

#path
path('addNewServices/',views.funNewServices,name='addNewServices'), 
# service booking details
path('serviceBookingDetails/',views.funserviceBook,name='serviceBookingDetails'),

]
