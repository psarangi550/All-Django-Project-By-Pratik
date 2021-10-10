from django.shortcuts import render

# Create your views here.
def my_temp_view(request):
    return render(request, "puppyApp/index.html")