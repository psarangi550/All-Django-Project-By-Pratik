from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    print("yes its working")
    return HttpResponse("Home View")

