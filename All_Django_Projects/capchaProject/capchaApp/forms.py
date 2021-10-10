from django import forms #importing  the forms module
from django.core import validators#importing the inbuild validator
from crispy_forms.helper import FormHelper #importing the form helper module from the
class StudentRegister(forms.Form):#creating the child class of Form class
    name=forms.CharField(label="Enter Your Name",widget=forms.TextInput(attrs={'class':"form-control" ,'placeholder':"Enter your Name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}),label="Enter Your Email")
    password=forms.CharField(label="Enter Valid Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Valid Password"}))
    cpassword=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))

    def clean(self):
        cleaned_data=super().clean()#fetching the cleaned data for all the field
        inputpass=cleaned_data["password"]
        inputcpass=cleaned_data["cpassword"]
        if inputpass != inputcpass:
            raise forms.ValidationError("Password MisMatch")

