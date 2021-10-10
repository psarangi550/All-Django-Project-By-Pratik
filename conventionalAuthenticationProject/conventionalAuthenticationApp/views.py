from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

@login_required(login_url="/login/")
def home_view(request):
    if request.user.is_authenticated:
        ip=request.session.get("ip","0.0.0.0")
        port=request.session.get("port","8000")
        return render (request,"conventionalAuthenticationApp/base.html",{"ip":ip,"port":port})
    else:
        return HttpResponseRedirect("/login/")


@login_required(login_url="/login/")
def pythondoc_view(request):
    return render (request,"conventionalAuthenticationApp/pythondoc.html",)
@login_required(login_url="/login/")
def djangodoc_view(request):
    return render (request,"conventionalAuthenticationApp/djangodoc.html",)
@login_required(login_url="/login/")
def flaskdoc_view(request):
    return render (request,"conventionalAuthenticationApp/flaskdoc.html",)

def login_view(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                user=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(username=user,password=password)
                if user is not None:
                    login(request,user)
                    next_page=request.GET.get("next",default="/home/")
                    return HttpResponseRedirect(next_page)
        else:
            form=AuthenticationForm()
        return render(request,"conventionalAuthenticationApp/login.html",{"form":form})
    else:
        # next_page=request.GET
        return HttpResponseRedirect("/home/")

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/login/")

def forgot_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/home/")
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request, "conventionalAuthenticationApp/password.html", {"form":form})
    else:
        return HttpResponseRedirect("/login/")



