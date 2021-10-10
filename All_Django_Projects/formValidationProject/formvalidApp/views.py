from django.shortcuts import render,HttpResponseRedirect
from .import forms
# Create your views here.

def thank_view(request):
    return render(request, "formvalidApp/thankyou.html")

def feedback_view(request):
    if  request.method=="GET":
        form=forms.Student_Feedback()
    if request.method == "POST":
        form=forms.Student_Feedback(request.POST)
        print(form)
        if form.is_valid():
            print("Validating the User Input and displaying to the console ")
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            rollno=form.cleaned_data["rollno"]
            feedback=form.cleaned_data["feedback"]
            my_dict={"name":name,"email":email,"rollno":rollno,"feedback":feedback}
            print(f'student Name is {form.cleaned_data.get("name")}')
            print(f'student Name is {form.cleaned_data.get("email")}')
            print(f'student Name is {form.cleaned_data.get("rollno")}')
            print(f'student Name is {form.cleaned_data.get("feedback")}')
        # return thank_view(request,form.cleaned_data.get("name"))
        return  HttpResponseRedirect("thanks/")
    return render(request, "formvalidApp/feedback.html", {"form":form})

