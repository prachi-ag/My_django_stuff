from django.contrib.auth.models import User
from django import forms
from . import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email',  'password', 'username')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ("profile_pic",)
