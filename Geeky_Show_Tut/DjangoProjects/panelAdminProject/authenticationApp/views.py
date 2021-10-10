from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm,PasswordChangeForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import SignUpForm,CustomUserChange,AdminUserChange
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

#signup view function
def signup_view(request):
    if request.user.is_anonymous:
        form=SignUpForm()
        if request.method=="POST":
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "SignUp Successfully")
        return render(request, "authenticationApp/signup.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")

#login view function
def login_view(request):
    if request.user.is_anonymous:
        form=AuthenticationForm()
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/profile/")
        return render(request, "authenticationApp/login.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")

#logout_view function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")

#profile_view function
def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "authenticationApp/profile.html")
    else:
        return HttpResponseRedirect("/login/")
#setPassword_view
def setpass_view(request):
    if request.user.is_authenticated:
        form=SetPasswordForm(user=request.user)
        if request.method == "POST":
            form=SetPasswordForm(request.user,request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return HttpResponseRedirect("/profile/")
        return render(request, "authenticationApp/setpass.html", {"form":form})
    else:
        return HttpResponseRedirect('/login/')

#password_change_form_view
def passchange_view(request):
    if request.user.is_authenticated:
        form=PasswordChangeForm(user=request.user)
        if request.method == "POST":
            form=PasswordChangeForm(request.user,request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return HttpResponseRedirect("/profile/")
        return render(request, "authenticationApp/setpass.html", {"form":form})
    else:
        return HttpResponseRedirect('/login/')


#userChangeForm
def userchange_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser==True:
                form=AdminUserChange(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                form=CustomUserChange(request.POST,instance=request.user)
                users=None
            if form.is_valid():
                form.save()
                messages.success(request,"User Details Changed")
                # update_session_auth_hash(request,form.user)
                # return HttpResponseRedirect("/profile/")
        else:
            if request.user.is_superuser==True:
                form=AdminUserChange(instance=request.user)
                users=User.objects.all()
            else:
                form=CustomUserChange(instance=request.user)
                users=None
        return render(request, "authenticationApp/userchange.html", {"form":form,"users":users})
    else:
        # messages.error(request, "please login First")
        return HttpResponseRedirect('/login/')

def userdetails_view(request,id):
    # if request.user.is_authenticated:
        if request.method=="POST":
            my_user=User.objects.get(pk=id)
            form=AdminUserChange(instance=my_user,data=request.POST)
            if form.is_valid():
                    form.save()
        else:
            my_user=User.objects.get(pk=id)
            form=AdminUserChange(instance=my_user)
        return render(request, "authenticationApp/userdetails.html", {"form":form})
