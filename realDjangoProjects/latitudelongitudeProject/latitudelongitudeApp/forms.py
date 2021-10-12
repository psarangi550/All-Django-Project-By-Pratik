from django import forms#importing the forms from django module
from .models import LatLong #importing the model class
class LatLongForm(forms.ModelForm):
    class Meta:
        model=LatLong
        fields="__all__"
