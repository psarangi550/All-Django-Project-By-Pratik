from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MyTemplateDynamicontextView(TemplateView):
    template_name="TemplateViewApp4/dynamic.html"
    def get_context_data(self, **kwargs):
        id=kwargs.get("id")
        # context =
        # context["name"]="Rika"
        # context["salary"]=50000
        # context["id"]=id
        context={"context":super().get_context_data(**kwargs),"name":"Rika","salary":5000,"id":id}
        return context
