from django import forms# importing the forms module from django module
from chucknorrisApp.models import Chuck_Choice
class ChuckForm(forms.ModelForm):
    class Meta:
        model=Chuck_Choice
        fields="__all__"
        labels={"category":"Select a Category"}
        widget={"category":forms.Select(attrs={"class":"form-select"})}

