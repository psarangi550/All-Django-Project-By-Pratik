from django import forms #importing the forms from django module
from django.core import validators #importing validator module from django.core module
#here creating the forms class with the form field inside it

def starter_name(value):
    if value[0].upper() !="A":
        raise forms.ValidationError("Name Should Starts with A")
class StudentRegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),validators=[starter_name])
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    feedback=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

    def clean(self):
        cleaned_data = super().clean()
        inputpass=cleaned_data.get("password")
        inputcpass=cleaned_data.get("cpassword")
        if inputpass != inputcpass:
            raise forms.ValidationError("Password Not Matching")
        return cleaned_data
