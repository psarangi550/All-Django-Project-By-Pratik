from django.contrib.auth.forms import UserCreationForm,UserChangeForm#import the UserCreationForm
from django.contrib.auth.models import User#importing the User Model class
from django import forms #importing the forms
class SignUpForm(UserCreationForm):#creating Our Own Model form class derived from UserCreation form
    username=forms.CharField(help_text='')
    class Meta(UserCreationForm.Meta):
        fields=("username","first_name","last_name","email")
        labels={"email":"Email ID"}
class CustomUserChange(UserChangeForm):
    password=None
    class Meta(UserCreationForm.Meta):
        fields=("username","first_name","last_name","email")

