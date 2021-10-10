from django import forms #importing the forms from the django module 
class Student(forms.Form):#creating the child class of Parent class Form 
    name=forms.CharField()
    email=forms.EmailField()
    key=forms.CharField(widget=forms.HiddenInput())
