from django.contrib import admin
from django.urls import path, include

from .views import  *
#import my_users, patient


urlpatterns = [
    path('rv_form/', rv_form_view.as_view(), name='rv_form'),
    path('rv_view/<str:key>', rv_view.as_view(), name='rv_view'),
    path('all_rv/', all_rv.as_view(), name='all_rv'),
#    path('clean_rv/', all_rv.clean_rv(), name='clean_rv'),

]
