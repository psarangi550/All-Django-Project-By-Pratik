from django import forms#importing the forms from the django module
import re #importing regular expression
#here we have to define the form class with form field
class StudentRegister(forms.Form):#child class of form.Form class
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    rollno=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))
    feedback=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean_email(self):#instance method for describing the validation
        input_email=self.cleaned_data.get('email')
        #fetching the input datata provided by the user by using the cleaned_data dictionary
        with open("jaradFormProject/invalidemail.txt","r") as f:
            spammer_email=f.readlines()
            for spam in spammer_email:
                if spam in input_email:
                    raise forms.ValidationError('invalid email')
        return input_email

