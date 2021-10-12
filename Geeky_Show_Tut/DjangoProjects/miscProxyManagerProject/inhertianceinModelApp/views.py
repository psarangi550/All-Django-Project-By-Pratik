from django.shortcuts import render
from .models import Student,ProxyStudent
# Create your views here.
def index_view(request):
    infos=ProxyStudent.custom.all()
    stus=Student.objects.all()
    return render (request,"inhertianceinModelApp/index.html",{"stus":stus,"infos":infos})
