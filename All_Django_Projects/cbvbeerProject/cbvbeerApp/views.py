from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from .models import Beer
from django.urls import reverse_lazy
# Create your views here.
class beerlist_view(ListView):
    model=Beer
class beerdetail_view(DetailView):
    model=Beer
class beercreate_view(CreateView):
    model=Beer
    fields="__all__"
class beerupdate_view(UpdateView):
    model=Beer
    fields=("price","taste","percentage_of_alchol","manufacture","is_alcholic")

class beerdelete_view(DeleteView):
    model=Beer
    success_url=reverse_lazy("home")

