from django.shortcuts import render
from . import forms #importing the forms where we declared the form
# Create your views here.
def form_view(request):
    #now we habve to create the object of the form class which we defined in the forms.py
    form=forms.StudentRegister()#creating the object of the form class we defined in forms.py file
    return render(request, 'formsApp/index.html', {'form':form})
    #sending the request to the template file with the form object we created out of the form
