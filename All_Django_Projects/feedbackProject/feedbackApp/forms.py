from django import forms
#importing the forms from the django module
class StudentFeedback(forms.Form):#creating the child class of the Forms class which is the child class of Form class
    name=forms.CharField()
    email=forms.EmailField()
    marks=forms.CharField()
    feedback=forms.CharField(widget=forms.Textarea)
    


