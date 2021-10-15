from django.shortcuts import render
from django.views.generic.list import ListView #importing the ListView class  used to render
from .models import Employee
# Create your views here.

class MyListView(ListView):#importing the ListView class  and creating the child of it
    # model=Employee
    queryset=Employee.objects.all()
    #here the default template is <model_name>_list.html
    #here the default context object being <model_name>_list
    #overrising the default value
    # template_name="ListViewApp/employee.html"#:-In this case both the template will be rendered
    # context_object_name="employees"
    ordering=("ename",)
    template_name_suffix="_get"
    # allowe_empty=False

    def get_queryset(self):
        return super().get_queryset().order_by("eno").filter(eno__gt=30)

