from django.shortcuts import render

# Create your views here.
def index_view(request,my_id,my_sub_id):
    my_id=my_id+1
    my_sub_id=my_sub_id+" documentation"
    return render(request, "urldynamicApp/index.html", {"my_id":my_id ,"my_sub_id":my_sub_id})
def home_view(request):
    return render(request, "urldynamicApp/home.html")
