# from django import forms #importing the forms module from the django module
from .models import Movie#copying the movie class from the models module
import floppyforms.__future__ as forms
#creating the model based form here
class movieRegister(forms.ModelForm):#creating the sub class of ModelForm class
    class Meta:
        widgets={"relese_date":forms.DateTimeInput(attrs={"id":"datepicker"})}
        model=Movie
        fields="__all__"

