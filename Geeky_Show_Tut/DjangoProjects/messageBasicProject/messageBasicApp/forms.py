from django import forms
from .models import Signup #importing the model class
#here we have to define our own Model class based on the SignUp Model
class SignUpForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields = "__all__"
