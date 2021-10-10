from django.shortcuts import render

# Create your views here.
from django.shortcuts import render #importing the render function
from .forms import  EmployeeForm #importing the SignUpForm Class
#creating the view function over here
def signup_view(request):#view function with request object
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
    else:
        form=EmployeeForm()
    return render(request, "passwordHasherApp/signup.html", {"form":form})

