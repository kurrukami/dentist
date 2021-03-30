from django.contrib import admin
from django.urls import path, include
#import my_users
from .views import *

urlpatterns = [
    path('all_patients', patients_gestion_page.as_view(), name='all_patients'),
    path('add_new_patient/', add_new_patient.as_view(), name='add_new_patient'),
    path('all_patients/serching', patients_gestion_page.as_view(), name='search_by_name'),
    path('delete_patient_real/?p<int:pk>[0-9]+', delete_patient_real, name='delete_patient_real'),
    path('delete_patient_fake/?p<int:pk>[0-9]+', patients_gestion_page.delete_patient_fake, name='delete_patient_fake'),
    path('update_patient/?p<int:pk>[0-9]+', update_patient2, name='update_patient'),



    ]
