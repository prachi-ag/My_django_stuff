from django.contrib.auth.models import User
from django import forms
from . import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length = 100)
    username = forms.CharField(max_length = 50)
    institute_name = forms.CharField(max_length= 200)



    class Meta:
        model = User
        fields = ( 'username', 'institute_name', 'password', 'email')


