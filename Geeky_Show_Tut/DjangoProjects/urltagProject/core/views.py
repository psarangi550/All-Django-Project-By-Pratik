from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "core/home.html",{"name":"home"})

def about_view(request):
    return render (request, "core/about.html")
