from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,SetPasswordForm,PasswordChangeForm,UserChangeForm #importing all the forms
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash #importing the methods for auyth module
from django.contrib import messages#importing the messages
from .forms import CustomUserChange
# Create your views here.
from .signup import SignUpForm


#for the sign up view
def signup_view(request):
    if request.user.is_anonymous:
        form=SignUpForm()
        if request.method == 'POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Signup Successful")
        return render(request, "resetPassBasicApp/signup.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")

#for the Login  view
def login_view(request):
    if request.user.is_anonymous:
        form=AuthenticationForm()
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(username=uname,password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "logged in Successfully")
                    return HttpResponseRedirect("/profile/")
        return render(request, "resetPassBasicApp/login.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")


#profile page view
def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "resetPassBasicApp/profile.html", {"name":request.user,"first_name":request.user.first_name,"last_name":request.user.last_name, "email":request.user.email})
    #rendering the info as its saved in the session
    else:
        return HttpResponseRedirect("/login/")


#log_out_view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")
    #redirrecting to the login page

def set_password_view(request):
    if request.user.is_authenticated:
        form=SetPasswordForm(request.user)
        # print(form)
        if request.method=="POST":
            form=SetPasswordForm(request.user,request.POST)
            print(form.user)
        # print(form)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return HttpResponseRedirect('/profile/')
        return render(request, "resetPassBasicApp/setpass.html", {"form":form})
    else:
        return HttpResponseRedirect("/login/")

def password_change_view(request):
    if request.user.is_authenticated:
        form=PasswordChangeForm(user=request.user)
        if request.method=="POST":
            form=PasswordChangeForm(request.POST,user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)#maining the same session
                return HttpResponseRedirect("/profile/")
        return render(request,"resetPassBasicApp/changepass.html",{"form":form})
    else:
       return HttpResponseRedirect("/login/")

#user change form
def user_change_view(request):
    form=UserChangeForm(instance=request.user)
    if request.method=="POST":
        form=UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/")
    return render(request, "resetPassBasicApp/userchange.html", {"form":form})
