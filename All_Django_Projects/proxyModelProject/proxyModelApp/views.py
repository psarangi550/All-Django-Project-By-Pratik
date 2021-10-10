from django.shortcuts import render
from .models import Employee,ProxyEmployee
# Create your views here.
def index_view(request):
    # emps=Employee.objects.all()
    # emps=Employee.objects.all()
    # emps=ProxyEmployee.objects.all()
    emps=Employee.custom.all()
    return render(request, "proxyModelApp/index.html", {"emps":emps})
