from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def index_view(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            stu=Student(name=name,email=email)
            stu.delete()
    return render(request, "modelSignalApp/index.html", {"form":form})

def confirm_view(request):
    render(request, "modelSignalApp/confirm.html")
