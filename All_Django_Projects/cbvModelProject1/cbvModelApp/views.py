from django.shortcuts import render
from cbvModelApp.models import Books
from django.views.generic import ListView,DetailView

# Create your views here.

class Booklist_view(ListView):#creating the child class of ListView Class
    model=Books #asssociatting the model
    #default_template_name=books_list.html
    #default_context_data=books_list
    #hence we have to render these default page

class BookDetails_view(DetailView):#creating the child class of DetailView Class
    model=Books#defining the model for the same
    #default_Template_Pack=books_detail.html
    #default_context_data=books or objects
