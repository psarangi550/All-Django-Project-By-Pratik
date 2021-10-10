from django.shortcuts import render
from .models import Employee

# Create your views here.
def index_view(request):
    emps=Employee.objects.all()
    # emps=Employee.employees.get_emp_range(2000,7000)
    return render(request, "modelManagerApp/index.html", {"emps":emps})
