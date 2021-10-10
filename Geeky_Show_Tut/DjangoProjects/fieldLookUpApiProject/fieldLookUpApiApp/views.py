from django.shortcuts import render
from .models import Employee
from datetime import datetime,date,time
# Create your views here.
def index_view(request):
    # emps=Employee.objects.all()
    # emps=Employee.objects.filter(edatetime__date__gt=date(1990,1,1))
    # emps=Employee.objects.filter(edatetime__time__lt=time(14,00,00))
    # print(emps.query)
    emps=Employee.objects.filter(eno__isnull=True)
    print(emps)
    print("*****************************************")
    print(emps.query)
    return render(request, "fieldLookUpApiApp/index.html", {"emps":emps})
