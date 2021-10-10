from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home_view(request):
    return render(request,"jobApp/home.html")
def hyd_view(request):
    hyd_job_list=Hydjobs.objects.order_by("Date")
    my_dict={"hyd_job_list":hyd_job_list}
    return render(request,"jobApp/hydjobs.html",context=my_dict)
def bnglr_view(request):
    bnglr_job_list=Bnglrjobs.objects.all()
    my_dict={"bnglr_job_list":bnglr_job_list}
    return render(request,"jobApp/bnglrjobs.html",context=my_dict)
def pune_view(request):
    pune_job_list=Punejobs.objects.all()
    my_dict={"pune_job_list":pune_job_list}
    return render(request,"jobApp/punejobs.html",context=my_dict)
def mumbai_view(request):
    mumbai_job_list=Mumbaijobs.objects.all()
    my_dict={"mumbai_job_list":mumbai_job_list}
    return render(request,"jobApp/mumbaijobs.html",context=my_dict)
# def insert_view(request):
#     durgajobsProject.insertdatadb.prepare(25)


