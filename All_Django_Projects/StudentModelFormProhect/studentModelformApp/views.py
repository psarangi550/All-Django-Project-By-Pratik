from django.shortcuts import render
from .import forms #importing the forms module from the same directory
from .models import Student #importing the models module
# Create your views here.

def thankyou_view(request):
    student_list=Student.objects.all()
    #fetching the query set Objects
    my_dict={"student_list":student_list}
    return render(request, "studentModelformApp/thankyou.html",context=my_dict)

def index_view(request):
    if request.method == 'GET':
        form=forms.StudentForm()#creating the object of form class
    if request.method=="POST":
        form=forms.StudentForm(request.POST)
        #creating the form object with user Provided data
        if form.is_valid():#here checking the validation
            print("The Student Name is" , form.cleaned_data.get("name"))
            print("The Student Email is",form.cleaned_data.get("email"))
            print("The Student Password is",form.cleaned_data.get("password"))
            print("The Student CPassword is",form.cleaned_data.get("cpassword"))
            form.save(commit=True)#saving the form to the Database Table
            return thankyou_view(request)
    return render(request, "studentModelformApp/index.html", {"form":form})


