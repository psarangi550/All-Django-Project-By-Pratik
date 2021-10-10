from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .signals import login_count_signal
from django.core.cache import cache

# Create your views here.
def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=uname,password=password)
            if user is not None:
                login(request, user)
                # count=cache.get("count")
                return HttpResponseRedirect("/index/")
    else:
        form=AuthenticationForm()
    return render(request, "loginCountApp/login.html", {"form": form})

def index_view(request):
    # cache.set(key="count",value=newcount)
    count=cache.get("count",version=request.user.id)
    return render(request, "loginCountApp/index.html",{"count":count})
def logout_view(request):
    update_session_auth_hash(request, request.user)
    logout(request)
    return HttpResponseRedirect("/login/")
