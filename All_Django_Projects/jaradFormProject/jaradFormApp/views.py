from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from . import forms
# Create your views here.

def thankyou_view(request):
    print(request.POST)
    return render (request,"jaradFormApp/thankyou.html")

def feedback_view(request):
    # form=forms.StudentRegister(request.POST or None)
    if request.method == 'POST':
        form=forms.StudentRegister(request.POST)
        print(form)
        if form.is_valid():
            print("Validation successfull")
            print(f'Student Name :-{form.cleaned_data["name"]}')
            print(f'Student Email:-{form.cleaned_data["email"]}')
            print(f'Student Roll No:-{form.cleaned_data["rollno"]}')
            print(f'Student Feedback:-{form.cleaned_data["feedback"]}')
            print(f'Student Feedback:-{request.POST["feedback"]}')
            return HttpResponseRedirect("thankyou/")
            # return thankyou_view(request,form.cleaned_data)
            # return render (request,"jaradFormApp/thankyou.html",{"name":form.cleaned_data["name"]})
    if request.method=="GET":
        form=forms.StudentRegister()
    return render(request, "jaradFormApp/index.html", context={"form":form})


