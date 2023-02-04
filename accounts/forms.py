from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200,required=False)
    last_name = forms.CharField(max_length=200,required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]
