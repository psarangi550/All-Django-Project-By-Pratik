from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages#importing the messages module
from django.contrib.auth import authenticate,login,logout
#here we are importing the user creattion Form nad Authenticate form
# Create your views here.

#signup_view function
def signup_view(request):
    if request.user.is_anonymous:
        form=UserCreationForm()#creating the object of UserCreationForm
        if request.method=="POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully signed Up")
        return render(request, "loginBasicApp/signup.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")


#login_view function
def login_view(request):
    if not request.user.is_authenticated:
        form=AuthenticationForm()#creating the object of UserCreationForm
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(username=uname,password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully")
                    return HttpResponseRedirect("/profile/")
        return render(request, "loginBasicApp/login.html", {"form":form})
    else:
        return HttpResponseRedirect("/profile/")

#profile functionality or profile view
def profile_view(request):
    # print(request.user)
    # print(request.session)
    if request.user.is_authenticated:
        return render(request, "loginBasicApp/profile.html",{"name":request.user})
    else:
        return HttpResponseRedirect("/login/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")
