from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome_test1(request):
    s="<h1>Welcome to Test1 Application </h1>"
    return HttpResponse(s)

