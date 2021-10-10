from django.shortcuts import render
from . import forms #importing the forms from current working directory
# Create your views here.
def index_view(request):#view function  with  request object
    if request.method=="GET":
        form=forms.StudentLogin()
        form.order_fields(field_order=["email","name"])#here we want to set that first email field then the name field
    if request.method=="POST":
        form=forms.StudentLogin(request.POST)
        #creatng the form object with the request forld 
        #this is actually not necessart over here 
    return render(request, 'geekApp40/index.html', {"form":form})
