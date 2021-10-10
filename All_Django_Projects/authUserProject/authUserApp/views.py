from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from authUserApp.login import Login_Form
from authUserApp.models import SignUpForm
# Create your views here.
def home_view(request):
    return render(request, "authUserApp/home.html")

@login_required(redirect_field_name="/python/",login_url='/login/')
def python_view(request):
    return render(request, "authUserApp/pythondoc.html")
# @login_required
def django_view(request):
    return render(request, "authUserApp/djangodoc.html")
# @login_required
def flask_view(request):
    return render(request, "authUserApp/flaskdoc.html")

def login_view(request):
    form=Login_Form()
    if request.method == "POST":
        pass
    return render(request, "authUserApp/login.html", {"form":form})
