from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#defining the Custom Template View With Contect and Extra context in as_view()
class MyTemplateContextView(TemplateView):
    template_name="TemplateViewApp3/display.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #here we are fetching the parent class contect object which is a dictionary
        print(context)#printing to the console
        context["name"]="pratik"
        context["salary"]=1000
        return context #returning the context object at the end
        #we have to pass the extra_context in the urls.py file
        #here we can add context as dictionaryu but only caveat is extra_context will not work in as_view()


