from django.shortcuts import render
from .models import Student,CommonInfo
# Create your views here.
def index_view(request):
    infos=CommonInfo.objects.all()
    stus=Student.objects.all()
    return render (request,"inhertianceinModelApp/index.html",{"stus":stus,"infos":infos})
