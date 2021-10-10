from django.shortcuts import render

# Create your views here.
def django_view(request):
    return render( request, "course/django.html")
