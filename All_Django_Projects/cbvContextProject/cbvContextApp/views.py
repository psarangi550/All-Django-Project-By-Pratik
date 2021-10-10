from django.shortcuts import render
from  django.views.generic import TemplateView
# Create your views here.
class Context_View(TemplateView):
    template_name="cbvContextApp/index.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["name"]="Abismtuta"
        context["Age"]=25
        context["email"]="rika1997@gmail.com"
        return context
