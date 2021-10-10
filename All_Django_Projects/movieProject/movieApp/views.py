from django.shortcuts import render
from movieApp.models import Movie
from movieApp.forms import movieRegister
# Create your views here.
def index_view(request):
    return render(request, "movieApp/index.html")
def addmovies_view(request):
    form=movieRegister()
    if request.method == "POST":
        form=movieRegister(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request, "movieApp/addmovies.html", {"form":form})
    #creating the addmovies form template and on the submit requerst redirecting to the index page
def listmovie_view(request):#view function with request object
    movie_list=Movie.objects.all()#fetching the QuerySet Object for the same
    return render(request, "movieApp/listmovies.html",{"movie_list": movie_list})
    #returning the list movies view function


