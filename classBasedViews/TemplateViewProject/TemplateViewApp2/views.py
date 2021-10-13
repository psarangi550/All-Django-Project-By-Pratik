from django.shortcuts import render
from django.views.generic import TemplateView #importing the template view
# Create your views here.


#defining the Custom Template View Class
class MyTemplateView(TemplateView):
    template_name="TemplateViewApp2/home.html"
