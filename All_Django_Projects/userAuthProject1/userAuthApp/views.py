from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import forms as f1
from . import forms
from .login import Login_Form
# Create your views here.
# @login_required()
def home_view(request):
    return render(request, "userAuthApp/home.html")

@login_required()
def python_view(request):
    return render(request, "userAuthApp/pythonexam.html")
@login_required
def django_view(request):
    return render(request, "userAuthApp/djangoexam.html")
@login_required
def flask_view(request):
    return render(request, "userAuthApp/flaskexam.html")

def login_view(request):
    form=Login_Form()
    if request.method=="POST":
        form=Login_Form(request.POST)
        if form.is_valid():
                return HttpResponseRedirect("/profile/")
    return render(request,"userAuthApp/login.html",{"form":form})


def logout_view(request):
    return render(request, "userAuthApp/logout.html")
def profile_view(request):
    # name=request.GET.get('name')
    # form2=f1.AuthenticationForm(request.POST)
    # name=request.GET.get("username")
    return render(request, "userAuthApp/profile.html",)
def signup_view(request):
    form1=forms.User_Form()
    if request.method == 'POST':
        form1=forms.User_Form(request.POST)
        if form1.is_valid():
            # password=form1.password
            # user=User(first_name=form1.first_name, password=form1.password, email=form1.email, last_name=form1.last_name, username=form1.username)
            # user.save()
            # user=form1.save()
            # user.set_password(user.password)
            # user.save()
            first_name=form1.cleaned_data["first_name"]
            last_name=form1.cleaned_data["last_name"]
            email=form1.cleaned_data["email"]
            username=form1.cleaned_data["username"]
            password=form1.cleaned_data['password']
            user=User(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect("/accounts/login")
    return render(request, "userAuthApp/signup.html", {"form":form1})
