from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm #importing the Sign Up form from the Forms.py file
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,update_session_auth_hash,logout,login
from django.contrib.auth.models import Group
# Create your views here.
def signup_view(request):
    if request.user.is_anonymous:
        form=SignUpForm()#creating the blank signUp form
        if request.method=="POST":
            form=SignUpForm(request.POST)
            if form.is_valid():
                user=form.save()
                group=Group.objects.get(name="Manager")
                user.groups.add(group)
                messages.success(request, "Sign Up Successful")
        return render(request,"groupPermissionApp/signup.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")

#login_view function
def login_view(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(username=uname,password=password)
                if user is not None:
                    messages.success(request,"Login Successful")
                    login(request,user)
                    return HttpResponseRedirect("/profile/")
        else:
            form=AuthenticationForm()
        return render(request, "groupPermissionApp/login.html", {"form":form})
    else:
        return HttpResponseRedirect('/profile/')

#defining the Profile View as
def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "groupPermissionApp/profile.html", {"name":request.user.username,"email":request.user.email,"first_name":request.user.first_name,"last_name":request.user.last_name})
    else:
        return HttpResponseRedirect("/login/")
#logout_view function
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/login/")



