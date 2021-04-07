from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('logout/', log_out, name='logout'),


    path('doctor_register/', doctor_register.as_view(), name='doctor_register'),

    path('superuser_page/', superuser_page, name='superuser_page'),
    path('admin_view/?p<str:key>/', admin_view.as_view(), name='admin_view'),
    path('get_adminn_pk/?p<str:username>/', get_adminn_pk, name='get_adminn_pk'),
    #path('get_adminn_pk/?p<int:pk>[0-9]+/', get_adminn_pk, name='get_adminn_pk'),
    path('delete_doctor_real/?p<int:pk>[0-9]+', delete_doctor_real, name='delete_doctor_real'),



    path('view/', view.as_view(), name='view'),
    path('send_infos_view1/', send_infos_view1.as_view(), name='send_infos1'),
    path('send_infos/', send_infos_view, name='send_infos'),
]
