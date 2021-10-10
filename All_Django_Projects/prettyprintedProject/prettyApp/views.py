from django.shortcuts import render
from .models import Student
# Create your views here.
def stu_view(request):
    stu_list_item=Student.objects.get()
    print(type(stu_list_item))
    my_dict={"stu_list_item":stu_list_item}
    return render(request,"prettyApp/index.html",context=my_dict)
