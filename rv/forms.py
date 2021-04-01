from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate, login
import datetime

from ze.shit import *

from django.contrib import messages
from my_users.models import *

#from django.utils.translation import gettext_lazy as _


class form_validationn(forms.Form):
    pass

"""
    def clean_doc_name(self):
        name = self.cleaned_data["doc_name"]
        try:
            n = doctor.objects.get(username=name)
            msg = f'doctor {name} was found'
            from_me_to_me(msg=msg)
        except doctor.DoesNotExist:
            msg = 'doctor u looking for is not here'
            from_me_to_me(msg=msg)
            raise forms.ValidationError(msg)
        return name

"""

from my_users.models import doctor

class rv_form_dt(forms.ModelForm):


    #doctors_list = list(filter(lambda x : x.username != 'kurru', doctor.objects.all()))
    #doctors = [(x.username.upper(), x.username) for x in doctors_list]

    #doctor = forms.ChoiceField(
    #    widget=forms.Select(attrs={'class':'select'}),
    #    choices=doctors
    #)


    year = forms.CharField(label='year', widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':'year'}))
    month = forms.CharField(label='month', widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':'month'}))
    day = forms.CharField(label='day', widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':'day'}))
    hour = forms.CharField(label='hour', widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':'hour'}))




    class Meta:
        model = rv
        fields = ['doc_name', 'name', 'phone_num', 'cmnt'
                  #'year', 'mounth', 'day', 'hour',
                 ]
        widgets = {

                   'doc_name': forms.TextInput(attrs={'class':'form_input', 'placeholder':'your doctor name'}),
                   'name': forms.TextInput(attrs={'class':'form_input', 'placeholder':'name'}),
                   'phone_num': forms.TextInput(attrs={'class':'form_input', 'placeholder':'phone'}),
                   'cmnt': forms.TextInput(attrs={'class':'form_input', 'placeholder':'comment', 'rows' :'1'}),

                   #'year': forms.TextInput(attrs={'class':'input is-primary is-medium', 'placeholder':'genre_visite'}),
                   #'month': forms.TextInput(attrs={'class':'input is-primary is-medium', 'placeholder':'montant a payer'}),
                   #'day': forms.TextInput(attrs={'class':'input is-primary is-medium', 'placeholder':'montant paye'}),
                   #'hour': forms.TextInput(attrs={'class':'textarea is-primary is-medium', 'placeholder':'commentaire'}),
        }


class rv_form_tmrw(forms.ModelForm, form_validationn):

    #doctors_list = list(filter(lambda x : x.username != 'kurru', doctor.objects.all()))
    #doctors = [(x.username.upper(), x.username) for x in doctors_list]

    #doctor = forms.ChoiceField(
    #    widget=forms.Select(attrs={'class':'select'}),
    #    choices=doctors
    #)

    hour = forms.CharField(label='hour', widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':'hour'}))


    class Meta:
        model = rv
        fields = ['doc_name','name', 'phone_num', 'cmnt'
                  #'year', 'mounth', 'day', 'hour',

                ]
        widgets = {
                   'doc_name': forms.TextInput(attrs={'class':'form_input', 'placeholder':'name'}),
                   'name': forms.TextInput(attrs={'class':'form_input', 'placeholder':'name'}),
                   'phone_num': forms.TextInput(attrs={'class':'form_input', 'placeholder':'phone'}),
                   'cmnt': forms.TextInput(attrs={'class':'form_input', 'placeholder':'comment', 'rows' :'1'}),




                   #'year': forms.TextInput(attrs={'class':'input is-primary is-medium', 'placeholder':'genre_visite'}),
                   #'month': forms.TextInput(attrs={'class':'input is-primary is-medium', 'placeholder':'montant a payer'}),
                   #'day': forms.TextInput(attrs={'class':'input is-primary is-medium', 'placeholder':'montant paye'}),
                   #'hour': forms.TextInput(attrs={'class':'textarea is-primary is-medium', 'placeholder':'commentaire'}),
        }
