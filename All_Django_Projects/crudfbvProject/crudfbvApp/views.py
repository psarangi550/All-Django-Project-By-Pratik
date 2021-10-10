from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def home_view(request):
    employees=Employee.objects.all()
    return render(request,"crudfbvApp/index.html", {"employees":employees})

#Insert a New Record
def insert_view(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    return render(request, "crudfbvApp/create.html", {"form":form})

#delete_view _configurations
def delete_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect("/home/")

#update_operation
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(data=request.POST,instance=employee)
        if form.is_valid():
            form.save()
        # eno=form.cleaned_data["eno"]
        # ename=form.cleaned_data["ename"]
        # esal=form.cleaned_data["esal"]
        # eaddr=form.cleaned_data["eaddr"]
        # emp=Employee.objects.get_or_create(instance=employee)
        # emp.save()
        return redirect("/home/")
    return render(request, "crudfbvApp/update.html", {"employee":employee})
