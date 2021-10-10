from django.shortcuts import render
from . import forms #importing the forms from current working fdirectory
# Create your views here.
def  index_view(request):
    if  request.method=="GET":
        form =forms.StudentRegister(auto_id=True)
    if request.method=="POST":
        form=forms.StudentRegister(request.POST)
        if form.is_valid():
            print(f"The Student Name is {form.cleaned_data.get('name')}")
    return  render(request, "geekApp39/index.html", {'form':form})
