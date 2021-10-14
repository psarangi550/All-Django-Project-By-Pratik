from django.shortcuts import render,HttpResponseRedirect
from .models import ToDoList
from .forms import ToDoListForm
from django.views.generic.base import TemplateView,RedirectView,View
# Create your views here.

#this class if for Add and Show the Task List

class TaskAddShowView(TemplateView):
    template_name="todolistApp/addshow.html"
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        form=ToDoListForm()
        todos=ToDoList.objects.all()
        context["form"]=form
        context["todos"]=todos
        return context
    def post(self,request):
        form=ToDoListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

#this class is for the deleting a task record using the RedirectView
class DelRedirectView(RedirectView):
    url="/"
    def get_redirect_url(self,*args,**kwargs):
        id=kwargs.get("id")
        ToDoList.objects.get(pk=id).delete()
        return super().get_redirect_url(*args,**kwargs)

#this will be used for the View Class of Base Class Based View

class UpdateTaskView(View):
    def get(self,request,id):
        task_id=ToDoList.objects.get(pk=id)
        form=ToDoListForm(instance=task_id)
        return render(request, "todolistApp/update.html" ,{"form":form})
    def post(self,request,id):
        task_id=ToDoList.objects.get(id=id)
        fm=ToDoListForm(request.POST,instance=task_id)
        if fm.is_valid():
            fm.save()
            # return render(request, "todolistApp/update.html" ,{"form":form})
            # date=form.cleaned_data["date"]
            # task=form.cleaned_data["date"]
            # task_description=form.cleaned_data["date"]
            # todo=ToDoList(date=date,task=task,task_description=task_description)
            # todo.save()
        return HttpResponseRedirect("/")


