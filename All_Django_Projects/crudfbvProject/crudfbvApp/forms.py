from django import forms #importing the forms.py file
from .models import Employee #importing the Employee model

class EmployeeForm(forms.ModelForm):#creating the modelForm
    class Meta:#Meta Inner class
        model=Employee
        fields="__all__"
