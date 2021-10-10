from django.shortcuts import render
from . import forms #importing the forms from the same directory
# Create your views here.
def index_view(request):
    if request.method=="GET":
        form=forms.StudentRegister()#cleating the object of empty studentRegister classes
    if request.method=="POST":
        form=forms.StudentRegister(request.POST)#cleating the object of user provided studentRegister classes
        if form.is_valid():
            print(f"The student name is {form.cleaned_data['name']}")
            print(f"The student name is {form.cleaned_data['email']}")
            print(f"The student name is {form.cleaned_data['rollno']}")
            print(f"The student name is {form.cleaned_data['password']}")
            print(f"The student name is {form.cleaned_data['cpassword']}")
    return render(request, "passwordApp/index.html", {"form":form})



