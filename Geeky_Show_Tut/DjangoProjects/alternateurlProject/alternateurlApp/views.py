from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("<h1>I am Index view Function</h1>")

def thanks_view(request):
    return HttpResponse("<h1> I am Thanks View Function </h1>")
    