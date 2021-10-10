from django import forms
import re #importing the regular expression module
#importing the forms from the django module
class Student_Feedback(forms.Form):
    #creating the child class of Form class which is in forms module
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))#define the form field we required for the forms
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))#define the form field we required for the forms
    rollno=forms.IntegerField()#define the form field we required for the forms
    feedback=forms.CharField(widget=forms.Textarea)#define the form field we required for the forms

    def clean_name(self):#instance method for describing the validation
        input_name=self.cleaned_data["name"]
        #fetching the input datata provided by the user by using the cleaned_data dictionary
        pattern=".{4,}"#regular expression for the names
        match=re.search(pattern,input_name)
        if match is not None:
            return input_name
        else:
            raise forms.ValidationError("Tha Name Should be Greater than 4")


