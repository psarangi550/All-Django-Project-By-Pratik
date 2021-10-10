from django.shortcuts import render,HttpResponse
from django.views.generic import View,TemplateView #importing the View Class from generic module
# Create your views here.
class HelloWorld_view(View):#creating the child class of HelloWorld_view for which View is the Parent Class
    def get(self,request):
        return HttpResponse("<h1>Hello World</h1>")

class HelloWorldTemplate_view(TemplateView):#creating the child class of HelloWorld_view for which TemplateView is the Parent Class
    template_name="cbvHelloApp/index.html"
