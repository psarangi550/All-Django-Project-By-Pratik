from django.shortcuts import render
from .models import Student
# Create your views here.
def index_view(request):
    stus=Student.objects.all()
    return render (request,"inhertianceinModelApp/index.html",{"stus":stus})
