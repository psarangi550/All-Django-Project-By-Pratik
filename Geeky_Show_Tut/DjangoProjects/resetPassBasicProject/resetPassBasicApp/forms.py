from django import forms #importing the forms module
from django.contrib.auth.forms import UserChangeForm
#importing the User Change Form
from django.contrib.auth.models import User

#here we are describing the for as our own wish
class CustomUserChange(UserChangeForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
