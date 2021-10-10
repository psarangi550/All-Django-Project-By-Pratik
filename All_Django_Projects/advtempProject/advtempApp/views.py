from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "advtempApp/home.html")
def movies_view(request):
    return render(request, "advtempApp/movies.html")
def sports_view(request):
    return render(request, "advtempApp/sports.html")
def politics_view(request):
    return render(request, "advtempApp/politics.html")
