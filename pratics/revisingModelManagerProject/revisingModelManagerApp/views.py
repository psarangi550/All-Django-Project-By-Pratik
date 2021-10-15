from django.shortcuts import render
from .models import Employee
# Create your views here.

def index_view(request):
    emps=Employee.custom.all()
    return render(request, "revisingModelManagerApp/index.html", {"emps":emps})
