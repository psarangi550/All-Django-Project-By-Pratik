from django.shortcuts import render

# Create your views here.
def my_views(request):
    return render(request,'settingsApp/index.html')
