from django import  forms #import forms from django module
from .models import ToDoList

class DateInput(forms.DateInput):
    input_type="date"


class ToDoListForm(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields="__all__"
        widgets={
                "date":DateInput(attrs={"class":"form-control"}),
                "task":forms.TextInput(attrs={"class":"form-control"}),
                "task_decription":forms.Textarea(attrs={"class":"form-control"}),
                }

