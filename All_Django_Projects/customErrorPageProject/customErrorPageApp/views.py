from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    print(10/0)
    return HttpResponse("<h1> Welcome to the View Function</h1>")
