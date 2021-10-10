from django import forms

class Index_Form(forms.Form):
    name=forms.CharField(label="Enter a Name")

class Age_Form(forms.Form):
    age=forms.CharField(label="Enter your Age")

class GF_Form(forms.Form):
    gf=forms.CharField()
