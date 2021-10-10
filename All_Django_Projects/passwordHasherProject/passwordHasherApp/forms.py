from django.contrib.auth.models import User #importing the user model
from django import forms#importing the forms from the django module
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields=["username","password","first_name","last_name"]
