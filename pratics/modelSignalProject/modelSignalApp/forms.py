from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    identifier=forms.SlugField(disabled=True,required=False)
    class Meta:
        model=Student
        fields="__all__"
