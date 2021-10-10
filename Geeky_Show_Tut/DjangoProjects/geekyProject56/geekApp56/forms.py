from django import forms #importing the forms from the django module
from geekApp56.models import Student #importing the student class from the models module
#here we have to create the class of model forms 
class StudentRegister(forms.ModelForm):#creating the child class of ModelForm classes
    class Meta:#meta inner class 
        model=Student #taking the models as Student 
        fields="__all__"
        widgets={"password":forms.PasswordInput}
        labels={"password":"Enter Password"}
        help_text={"password":"Please provide a Password containing 8 digits"}
        
