from django.shortcuts import render
from .models import StudentTeacherRegistration
from .forms import TeacherRegister,StudentRegister
#importing both the Model Form classes to render differently
# Create your views here.
def student_view(request):
    form=StudentRegister()
    if request.method=="POST":
        form=StudentRegister(request.POST)
        if form.is_valid():
            student_name=form.cleaned_data["student_name"]
            # teacher_name=form.cleaned_data["teacher_name"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            stu=StudentTeacherRegistration(student_name=student_name,email=email,password=password)
            stu.save()#saving to the db
            form=StudentRegister()
    return render(request, "modelFormApp/student.html", {"form":form})

def teacher_view(request):
    form=TeacherRegister()
    if request.method=="POST":
        form=TeacherRegister(request.POST)
        if form.is_valid():
            # student_name=form.cleaned_data["student_name"]
            teacher_name=form.cleaned_data["teacher_name"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            tea=StudentTeacherRegistration(teacher_name=teacher_name,email=email,password=password)
            tea.save()#saving to the db
            form=TeacherRegister()
    return render(request, "modelFormApp/student.html", {"form":form})
