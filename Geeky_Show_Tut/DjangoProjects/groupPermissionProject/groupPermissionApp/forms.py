from django import forms #importing the forms module from django module
from django.contrib.auth.forms import UserCreationForm#importing the userCreation Form
from django.contrib.auth.models import User

#now we have to creat the form for the Sign Up from the UserCreation Form
class SignUpForm(UserCreationForm):#creating the child class of UserCreation form
    class Meta(UserCreationForm.Meta):#here inherting from the child class Meta
        fields = ("username", "first_name", "last_name", "email",)
