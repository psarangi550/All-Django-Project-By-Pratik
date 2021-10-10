from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    username=None
    # password2=None
    # password1=None
    # password1=forms.CharField(widget=forms.PasswordInput,help_text='')
    # password2=forms.CharField(label="Conf Password",widget=forms.PasswordInput)
    # username=forms.CharField(help_text="")
    class Meta(UserCreationForm.Meta):
        fields=["username","first_name", "last_name","email"]
        labels={"email":"Email ID","username":"UserName"}


