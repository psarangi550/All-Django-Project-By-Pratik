from django import forms #importing the forms module
from django.core import validators#importing the validators
from .models import Student #importing the models Module
class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=20,label="Enter Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}),label="Enter Email")
    password=forms.CharField(max_length=10,label="Enter Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    cpassword=forms.CharField(max_length=10,label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=Student
        fields="__all__"
    def clean(self):
        cleaned_data=super().clean()
        inputpass=cleaned_data["password"]
        inputcpass=cleaned_data["cpassword"]
        if inputpass != inputcpass :
            raise forms.ValidationError("Password mismatch")
