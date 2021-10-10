from django.shortcuts import render
from . import forms#importing the module from the current directory

# Create your views here.
def index_view(request):
    if request.method=="GET":
        form =forms.Student()
    return render(request,"geekApp41/index.html" , {'form':form})