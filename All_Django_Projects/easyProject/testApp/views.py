from django.shortcuts import render

# Create your views here.
def temp_view(request):
    return render(request,'testApp/index.html')
