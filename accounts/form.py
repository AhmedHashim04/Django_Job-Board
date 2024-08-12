from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


        


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']


class User_edit(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class Profile_edit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','tel','image']