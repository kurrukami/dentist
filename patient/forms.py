from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate, login
from ze.shit import *
from django.contrib import messages



class patient_form(forms.ModelForm):

    def clean_montant_paye(self):

        paye = self.cleaned_data["montant_paye"]
        a_paye = self.cleaned_data["montant_a_payer"]
        if paye>a_paye:
            msg = "cant be bigger than montant_a_payer"
            from_me_to_me(msg=msg)
            raise forms.ValidationError(msg)
        return paye

    """def clean_cin(self):

        cin = self.cleaned_data["cin"]
        try:
            c = patient.objects.get(cin=cin)
            msg = 'tht cin is alrady used, plz try ur own cin'
            from_me_to_me(msg=msg)
            raise forms.ValidationError(msg)
        except patient.DoesNotExist:
             return cin
        return cin"""


    class Meta:
        model = patient
        fields = ['name', 'phone_num', 'cin',
                  'genre_visite', 'montant_a_payer',
                  'montant_paye', 'commentaire'
                 ]
        widgets = {
                   'name': forms.TextInput(attrs={'class':'form_input', 'placeholder':'name'}),
                   'cin': forms.TextInput(attrs={'class':'form_input', 'placeholder':'cin'}),
                   'phone_num': forms.TextInput(attrs={'class':'form_input', 'placeholder':'phone'}),
                   'genre_visite': forms.TextInput(attrs={'class':'form_input', 'placeholder':'genre_visite'}),
                   'montant_a_payer': forms.TextInput(attrs={'class':'form_input', 'placeholder':'montant a payer'}),
                   'montant_paye': forms.TextInput(attrs={'class':'form_input', 'placeholder':'montant paye'}),
                   'commentaire': forms.TextInput(attrs={'class':'form_input', 'placeholder':'commentaire', 'rows': '5'}),
        }
