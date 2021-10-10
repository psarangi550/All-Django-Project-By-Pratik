from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyd_jobs_urls(request):
    s1="<h1>This is Hyderabad Related Job Information </h1>"
    return HttpResponse(s1)
def bang_jobs_urls(request):
    s2="<h1>This is Bangalore Related Job Information </h1>"
    return HttpResponse(s2)
def pune_jobs_urls(request):
    s3="<h1>This is Pune Related Job Information </h1>"
    return HttpResponse(s3)
def mumbai_jobs_urls(request):
    s4="<h1>This is Mumbai Related Job Information </h1>"
    return HttpResponse(s4)