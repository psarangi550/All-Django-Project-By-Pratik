from django.shortcuts import render
from .import forms #importing the forms module
# Create your views here.
def name_view(request):
    form1=forms.Name_Form()
    return render (request, "sessionformApp/name.html", {"form1":form1})
def age_view(request):
    form2=forms.Age_Form()
    form1=forms.Name_Form(request.GET)
    if form1.is_valid():
        name=form1.cleaned_data["name"]
        my_name=request.session.get("name","Guest")
        my_name=name
        request.session["name"]=my_name
    return render(request, "sessionformApp/age.html",{"form2":form2})
def gf_view(request):
    form3=forms.GF_Form()
    form2=forms.Age_Form(request.GET)
    if form2.is_valid():
        age=form2.cleaned_data["age"]
        my_age=request.session.get("age",0)
        my_age=age
        request.session["age"]=my_age
    return render(request, "sessionformApp/gf.html",{"form3":form3})
def result_view(request):
    form3=forms.GF_Form(request.GET)
    if form3.is_valid():
        gf=form3.cleaned_data["gf"]
        my_gf=request.session.get("gf","Abi")
        my_gf=gf
        request.session["gf"]=my_gf
    return render(request,"sessionformApp/result.html",{"name":request.session.get("name"),"age":request.session.get("age"),"gf":my_gf})

