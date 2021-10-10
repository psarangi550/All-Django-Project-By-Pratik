from django.shortcuts import render,HttpResponse
from . import forms#importing the form module created by us
import requests
import json
# Create your views here.

def thankyou_view(request,args):
    return render(request, "capchaApp/thankyou.html", context=args)
def index_view(request):
    if request.method=="POST":
        form=forms.StudentRegister(request.POST)
        if form.is_valid():
            clientKey=request.POST.get("g-recaptcha-response")
            secretKey="6LfWQEccAAAAAB6nmNjc2dEJ0cXBsejo17Keo4Jc"
            data={
                "secret":secretKey,
                "response":clientKey
            }
            resp=requests.post("https://www.google.com/recaptcha/api/siteverify",data=data)
            text=resp.text
            print(text)
            my_dict=resp.json()
            # print(my_dict)
            if my_dict["success"]==True:
                print(f'The student Name is {form.cleaned_data["name"]}')
                print(f'The student Email is {form.cleaned_data["email"]}')
                print(f'The student Password is {form.cleaned_data["password"]}')
                print(f'The student Password is {form.cleaned_data["cpassword"]}')
                return thankyou_view(request, {"name":form.cleaned_data["name"]})
                # print(type(my_dict))
            else:
                return HttpResponse("<h1>Validation Failed</h1>")

    if request.method == "GET":
        form=forms.StudentRegister()

    return render(request, "capchaApp/index.html",{"form":form,"cap":"6LfWQEccAAAAAJ69GoE39KUqG4mlzzy6U0ag029r"})
