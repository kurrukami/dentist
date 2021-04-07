from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate, login





class adminn_infos_form(forms.ModelForm):
    class Meta:
        model = adminn_infos
        fields = ('username', 'email', 'phone_num')
        widgets = {
                   'username': forms.TextInput(attrs={'class':'form_input', 'placeholder':'username'}),
                   'email': forms.TextInput(attrs={'class':'form_input', 'placeholder':'email'}),
                   'phone_num': forms.TextInput(attrs={'class':'form_input', 'placeholder':'phone'}),
        }


class doctor_register_form(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form_input', 'placeholder':'password'}))
    
    class Meta:
        model = doctor
        fields = ('username', 'email', 'phone_num')
        widgets = {
                   'username': forms.TextInput(attrs={'class':'form_input', 'placeholder':'username'}),
                   'email': forms.TextInput(attrs={'class':'form_input', 'placeholder':'email'}),
                   'phone_num': forms.TextInput(attrs={'class':'form_input', 'placeholder':'phone'}),
        }


class login_form(forms.Form):

    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':'username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form_input', 'placeholder':'password'}))#widget=forms.PasswordInput(attrs={'class':'input'}))
