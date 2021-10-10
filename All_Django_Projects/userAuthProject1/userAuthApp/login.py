from django import forms
from django.contrib.auth.models import User
class Login_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password",]
        help_text={"username": None }
        widgets={"password":forms.PasswordInput()}
        help_text={"username": ""}
    def clean(self):
        cleaned_data=super().clean()
        input_username=cleaned_data["username"]
        input_password=cleaned_data["password"]
        users=User.objects.all()
        for user in users:
            if input_username not in user.username:
                raise forms.ValidationError("invalid user")
        return input_username
        return input_username
