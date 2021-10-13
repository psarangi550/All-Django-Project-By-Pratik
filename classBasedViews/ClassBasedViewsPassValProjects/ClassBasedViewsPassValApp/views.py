from django.shortcuts import render,HttpResponse
from django.views import View #importing the View-Base Class Based View
from .forms import MyForm #importing the MyForm Class from forms.py file
# Create your views here.
class MyView(View):#creating the sub class of View Class
    name="pratik"
    def get(self,request):
        return HttpResponse(self.name)

class MySubView(MyView):#creating the subclass of my class
    def get(self,request):#overriding the Get Method
        return HttpResponse(self.name)
#############################################################################
#rendering Forms by the class Based View
class MyFormView(View):
    name="partik"
    def get(self,request):
        form=MyForm()
        return render(request,"ClassBasedViewsPassValApp/form.html", context={"form":form})
    def post(self,request):
        form=MyForm(request.POST)
        if form.is_valid():
            # self.name=form.cleaned_data["name"]
            return HttpResponse(self.name)

