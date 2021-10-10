from django.shortcuts import render
from . import forms #importing the forms from the same directory
# Create your views here.


def result_view(request,args):
    return render(request, "feedbackApp/thankyou.html", {"name":args})

def my_view(request):
    if request.method=="GET":
        form=forms.StudentFeedback()
        return render(request,"feedbackApp/index.html",{'form':form})
    if request.method=="POST":
        form=forms.StudentFeedback(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(f'Student Name is {form.cleaned_data["name"]}')
            print(f'Student Email is {form.cleaned_data["email"]}')
            print(f'Student Mark is {form.cleaned_data["marks"]}')
            print(f'Student Feedback is{form.cleaned_data["feedback"]}')
            my_dict={'name':form.cleaned_data["name"],'email':form.cleaned_data["email"]}
            return result_view(request,form.cleaned_data["name"])
            # return render(request, "feedbackApp/thankyou.html", {"name":form.cleaned_data["name"]})


