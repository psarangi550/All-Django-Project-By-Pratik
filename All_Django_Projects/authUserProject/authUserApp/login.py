from django import forms
from authUserApp.models import SignUpForm
class Login_Form(forms.ModelForm):
    class Meta:
        model=SignUpForm
        fields = ("username", "password")
        widgets={"password":forms.PasswordInput}
    # def clean(self):
    #     input_username=self.cleaned_data["username"]
    #     input_password=self.cleaned_data["password"]
    #     user=SignUpForm.objects.get(username=input_username)
    #     if input_username!=user.username:
    #         raise forms.ValidationError("Incoorect Username and Password")
    #     return input_username
    #     return input_password


