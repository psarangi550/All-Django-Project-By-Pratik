from django import forms #importing the form from the django module
from weatherApp.models import Weather
class WeatherForm(forms.ModelForm):
    class Meta:
        model=Weather
        fields=["name"]
        widgets={"name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your City Name"})}
        labels={"name":""}

