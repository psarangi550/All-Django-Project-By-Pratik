from django import forms #importing the forms module

class StudentRegister(forms.Form):#creating the sub class of forms.Form class
        name=forms.CharField()#here in the charfield max_length is not required
        mark=forms.IntegerField()#here this is for the integer field
        #here this wioll create the form widget with the name as name and mark which is the variabke name
