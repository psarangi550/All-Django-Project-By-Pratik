from django import forms #importing the forms from django module
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
#admin wiget form importing so that it can work well

class AdminForm(forms.Form):
    created_date=forms.DateTimeField(widget=AdminSplitDateTime)
    posted_date=forms.DateField(widget=AdminDateWidget)
    finished_time=forms.TimeField(widget=AdminTimeWidget)

