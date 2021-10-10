from django.shortcuts import render
from .import forms
# Create your views here.
def index_view(request):
    form=forms.Index_Form()
    return render(request,"sessionApp/index.html",{"form":form})
def add_view(request):
    form=forms.Index_Form()
    item_name=request.GET.get("item_name")
    item_quantity=request.GET.get("item_quantity")
    request.session[item_name]=item_quantity
    request.session.set_expiry(10)
    return render(request,"sessionApp/index.html",{"form":form})
def fetch_view(request):
    return render(request, "sessionApp/result.html")
