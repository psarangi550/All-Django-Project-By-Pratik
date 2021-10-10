from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book
# Create your views here.

class BookList_view(ListView):
    model=Book
    template_name="cbvModelViewCustomApp/book.html"
    context_object_name="list_of_book"

class BookDetails_View(DetailView):
    model=Book
    template_name="cbvModelViewCustomApp/bookdetails.html"
    #default_context_data="book"/"objects"
