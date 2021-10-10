from django.shortcuts import render
import datetime
# Create your views here.
def home_view(request):

    return render(request, "newsApp/home.html")
def movie_view(request):
    dt = datetime.datetime.now().strftime("%A:%B %d:%m:%Y %H:%M:%S %p")
    movie_news1 = "Once Django finished Watch Siderman Movie "
    movie_news2 = "Waiting for Upcoming Movie"
    my_dict = {"date": dt, "movie_news1": movie_news1, "movie_news2": movie_news2}
    return render(request, "newsApp/movie.html",context=my_dict)
def sport_view(request):
    dt = datetime.datetime.now().strftime("%A:%B %d:%m:%Y %H:%M:%S %p")
    sport_news1 = "Once Django finished Watch UFEA Champions League "
    sport_news2 = "Winning Champions league this year seems difficult for liverpool"
    my_dict = {"date": dt, "sport_news1": sport_news1, "sport_news2": sport_news2}
    return render(request, "newsApp/sport.html",context=my_dict)
def politics_view(request):
    dt = datetime.datetime.now().strftime("%A:%B %d:%m:%Y %H:%M:%S %p")
    politics_news1 = "Taliban now took Over Afgan"
    politics_news2 = "Presuming More threat to india"
    my_dict = {"date": dt, "politics_news1": politics_news1 , "politics_news2": politics_news2}
    return render(request, "newsApp/politics.html",context=my_dict)
