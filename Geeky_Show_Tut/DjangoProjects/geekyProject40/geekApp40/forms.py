from django import forms#importing the forms module from the django module 
class StudentLogin(forms.Form):#creating the child class of Form class
    name=forms.CharField()
    email=forms.EmailField()
    #now we want to set the order as Email and mail by using the order_filed() on the form object inside thye views.py file
