from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print(10/0)
    return HttpResponse("Welcome to home")
