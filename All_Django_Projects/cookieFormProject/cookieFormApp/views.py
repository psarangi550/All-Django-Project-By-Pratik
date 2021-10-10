from django.shortcuts import render
from . import forms #importing the forms from the Form Api
# Create your views here.
def index_view(request):
    form1=forms.Index_Form()
    return render(request, "cookieFormApp/index.html", {"form1": form1})
def age_view(request):
    form1=forms.Index_Form(request.GET)
    form2=forms.Age_Form()
    if form1.is_valid():
        name=form1.cleaned_data["name"]
        resp=render(request,"cookieFormApp/age.html",{"form2":form2})
        resp.set_cookie("name",name)
        return resp
    return render(request,"cookieFormApp/age.html",{"form2":form2})
def gf_view(request):
    form3=forms.GF_Form()
    form2=forms.Age_Form(request.GET)
    if form2.is_valid():
        age=form2.cleaned_data["age"]
        resp=render(request,"cookieFormApp/gf.html",{"form3":form3})
        resp.set_cookie("age",age)
        return resp
    return render(request,"cookieFormApp/gf.html",{"form3":form3})
def result_view(request):
    form3=forms.GF_Form(request.GET)
    gf=request.GET.get("gf")
    return render(request,"cookieFormApp/result.html",{"name":request.COOKIES.get("name"),"age":request.COOKIES.get("age"),"gf":gf})




