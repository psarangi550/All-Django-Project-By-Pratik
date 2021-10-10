from django import forms #import the forms from the django module
from django.core import validators #importing the validator from the django.core module
from .models import StudentTeacherRegistration #importuing the model class
class StudentRegister(forms.ModelForm):
    class Meta:
        model=StudentTeacherRegistration
        fields="__all__"
        # exclude=("teacher_name",)
class TeacherRegister(StudentRegister):#inheriting the Parent Model class StudentRegister
    class Meta(StudentRegister.Meta):#here also inheriting the Meta class of the parent
        fields=("teacher_name","email","password")
        validators={"teacher_name": validators.MinValueValidator(5) }
        student_name
