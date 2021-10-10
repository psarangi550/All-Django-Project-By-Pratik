from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_view(request):
    my_temp="blogApp/template.html"
    with open("./templates/blogApp/template.html") as f:
        data=f.read()
        return HttpResponse(data)
