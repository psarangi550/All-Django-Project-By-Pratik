from django import forms
from .models import School

class DateInput(forms.DateInput):
    input_type="date"

class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields=["name","roll","city","marks","pass_date"]
        widgets={"pass_date":DateInput()}
