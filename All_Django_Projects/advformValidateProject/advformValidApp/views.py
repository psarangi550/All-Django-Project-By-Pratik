from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.

def thank_view(request):
    return render(request,'advformValidApp/thankyou.html')
def index_view(request):
    if request.method=="GET":
        form=forms.StudentRegisterForm()#creating  form object with blank data
    if request.method=="POST":
        form=forms.StudentRegisterForm(request.POST)
        if form.is_valid():
            print('Validation completed Successfully')
            print(f'The student Name is {form.cleaned_data["name"]}')
            print(f'The student Email is {form.cleaned_data["email"]}')
            print(f'The Student Password is {form.cleaned_data["password"]}')
            print(f'The Student Password is {form.cleaned_data["cpassword"]}')
            return HttpResponseRedirect("thankyou/")

    return render(request, "advformValidApp/index.html", {"form":form})
