from django import forms #importing the forms module

class MyForm(forms.Form):#creating a Form Class Uisng the Form Api
    name=forms.CharField()
