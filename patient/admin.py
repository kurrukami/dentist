from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(patient)
class adminnAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'cin',
    'phone_num', 'genre_visite',
    'montant_a_payer', 'montant_paye',
    'commentaire','is_deleted',
    'date_debut', 'is_completed'
    )
