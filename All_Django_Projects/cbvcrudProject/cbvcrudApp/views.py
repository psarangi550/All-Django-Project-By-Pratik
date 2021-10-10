from django.shortcuts import render
from .models import  Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
import faker
import random
from django.urls import reverse_lazy
# Create your views here.

#listing Out the Book Details

class booklist_view(ListView):#creating the child class of ListView Class
    model=Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        element=random.choice(["bg-success","bg-danger","bg-info","bg-secondary","bg-warning"])
        context["element"]=element
        return context

#for individual Books
class bookdetail_view(DetailView):
    model=Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        element=random.choice(["bg-success","bg-danger","bg-info","bg-secondary","bg-warning"])
        context["element"]=element
        return context

#for CreateView for Inserting the New Records
class bookinsert_view(CreateView):
    model=Book
    fields="__all__"


#now for the UpdateView Functionality
class bookupdate_view(UpdateView):
    model=Book
    fields=["author","pages","price"]

#now for the DeleteView view function

class bookdelete_view(DeleteView):
    model=Book
    success_url=reverse_lazy("home")

