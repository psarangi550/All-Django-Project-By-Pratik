from django.shortcuts import render,HttpResponse
from  .models import Student
# Create your views here.
def index_view(request):
    stu=Student(roll=101,name="pratik",mark=96)
    stu.save()
    return HttpResponse("<h1> Data Added successfully</h1>")
