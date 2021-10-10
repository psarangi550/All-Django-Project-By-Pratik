from django.shortcuts import render
from chucknorrisApp.forms import ChuckForm
import requests
# Create your views here.
def index_view(request):
    if request.method=="POST":
        form=ChuckForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            category_value=form.cleaned_data["category"]
            url=f"https://api.chucknorris.io/jokes/random?category={category_value}"
            print(url)
            resp=requests.get(url)
            my_dict=resp.json()
            print(my_dict)
            my_value={"icon":my_dict["icon_url"],"value":my_dict["value"]}
        return render (request,"chucknorrisApp/index.html",{ "form":form ,"my_value":my_value})
    form=ChuckForm()
    return render(request, "chucknorrisApp/index.html",{"form":form})
