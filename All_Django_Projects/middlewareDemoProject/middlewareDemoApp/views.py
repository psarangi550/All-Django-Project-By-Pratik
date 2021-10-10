from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    print("this is the response from the view function")
    return HttpResponse("<h1>Lets See</h1>")
