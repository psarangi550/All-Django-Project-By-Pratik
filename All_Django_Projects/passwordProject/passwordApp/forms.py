from django import forms#importing the forms from the django module
from django.core import validators#importing the validators module from core module
from crispy_forms.helper import FormHelper
def starts_with_a(value):
    if value[0].lower() != "a":
        raise forms.ValidationError("Name should starts with a or A")


class StudentRegister(forms.Form):#creating the child class of the form class
    # required_css_class="required"
    helper=FormHelper()
    helper.form_show_labels=False;
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),help_text="Name should starts with a or A",required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}),help_text="Email Should be Gmail Only",required=True)
    rollno=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),help_text="Only Numbers Allowed",required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), help_text="Enter a valid password",required=True)
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), help_text="Please confirm password",required=True)

    def clean(self):
        cleaned_data=super().clean()
        inputpass=cleaned_data.get('password')
        inputcpass=cleaned_data.get('cpassword')
        if inputpass != inputcpass:
            raise forms.ValidationError("Wong Password")
        return cleaned_data.get

