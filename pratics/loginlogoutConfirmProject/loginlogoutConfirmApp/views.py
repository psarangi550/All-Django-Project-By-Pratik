from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=uname,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/index/")

    else:
        form=AuthenticationForm()
    return render (request, "loginlogoutConfirmApp/login.html", {"form":form})

def index(request):
    return render(request, "loginlogoutConfirmApp/index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")

# def confirm(request):
#     return render(request, "loginlogoutConfirmApp/confirm.html")
