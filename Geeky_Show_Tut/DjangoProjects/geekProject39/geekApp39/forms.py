from django import forms
#importing the form from the django module 
class StudentRegister(forms.Form):#creating the subclass of Form class 
    name=forms.CharField()
