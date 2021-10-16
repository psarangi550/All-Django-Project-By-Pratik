from django.shortcuts import render
from django.views.generic.list import ListView #importing the ListView class  used to render
from django.views.generic.detail import DetailView #importing the DetailView class  used to render
from .models import Employee
# Create your views here.

class MyListView(ListView):
    model=Employee
    template_name="ListViewApp/employee.html"




class MyDetailView(DetailView):
    model=Employee
    # queryset=Employee.objects.all()
    # template_name_field="_esal"
    pk_url_kwarg="id"
    #here will go for the next example where  we will be using the List View and Detail View Togrther
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["employee_list"]=Employee.objects.all()
        return context

























# class MyListView(ListView):#importing the ListView class  and creating the child of it
#     model=Employee
#     # queryset=Employee.objects.all()
#     #here the default template is <model_name>_list.html
#     #here the default context object being <model_name>_list
#     #overrising the default value
#     template_name="ListViewApp/employee.html"#:-In this case both the template will be rendered
#     # context_object_name="employees"
#     # ordering=("ename",)
#     # template_name_suffix="_get"
#     # allow_empty=False
#     #usage of get_queryset()
#     # def get_queryset(self):
#     #     return super().get_queryset().order_by("eno").filter(eno__gt=30)
#     # #usage od get_context_data
#     # def get_context_data(self,*args,**kwargs):
#     #     context = super().get_context_data(*args,**kwargs)
#     #     context["filters"]=Employee.objects.filter(ename="Anahi Rama")
#         # return context #returning the context objects in here
#     #usage_of get_template Name:-Based on the cookies
#     def get_template_name(self):#this wll always return a list of templates
#         # if self.request.COOKIES["name"]=="Rika":
#         if self.request.user.is_superuser():
#             template_name="ListViewApp/index.html"
#         else:
#             template_name=self.template_name
#         return [template_name] #returning the list of template name




