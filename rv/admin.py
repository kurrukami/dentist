from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(rv)
class rva_dmin(admin.ModelAdmin):
    list_display =  ['doc_name','name', 'phone_num', 'cmnt',
                     'rd_time'

             ]
