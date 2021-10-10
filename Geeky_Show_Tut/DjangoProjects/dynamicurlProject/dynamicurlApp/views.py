from django.shortcuts import render

# Create your views here.
def index_view(request,my_year):
    student={"my_year":my_year}
    return render(request, "dynamicurlApp/index.html", context=student)
def home_view(request):
    return render(request, "dynamicurlApp/home.html")
