from django.contrib import admin

# Register your models here.


from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class adminnAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_num', 'type', 'is_admin', 'get_created_time', 'get_last_login')


@admin.register(adminn)
class adminnAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_num', 'type', 'is_admin', 'get_created_time', 'get_last_login')

@admin.register(doctor)
class adminnAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_num', 'type', 'is_admin', 'get_created_time', 'get_last_login')


@admin.register(adminn_infos)
class adminn_infos(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_num', 'created')
