from django.urls import path, include
from .views import *
#import my_users, patient



urlpatterns = [
    path('welcome/?p<str:key>', home_pages.as_view(), name='home'),
    path('', home, name='enter'),

    ]
