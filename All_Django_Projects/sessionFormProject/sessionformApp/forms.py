from django import forms #importing the forms for Form API

class Name_Form(forms.Form):
    name=forms.CharField(label="Enter Your Name")

class Age_Form(forms.Form):
    age=forms.IntegerField(label="Enter your age")

class GF_Form(forms.Form):
    gf=forms.CharField(label="Enter Your GF Name")
