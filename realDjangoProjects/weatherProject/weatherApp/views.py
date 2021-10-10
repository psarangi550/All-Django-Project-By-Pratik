from django.shortcuts import render
import requests #import the requests module
from weatherApp import models
from weatherApp import forms
# name="Odisha"

# Create your views here.
def index_view(request):
    #for Displaying All the city info
    # city_list=models.Weather.objects.all()
    # weather_app=[]
    # for citi in city_list:
    #     name=citi
    #     key="667fea17e45960efd542e3fdfc3dd9d6"
    #     url=f"https://api.openweathermap.org/data/2.5/weather?q={name}&units=metric&appid={key}"
    #     resp=requests.get(url)
    #     dict1=resp.json()#fetching the python dictionary from the url
    #     my_dict={
    #         "name":dict1["name"],
    #         "temp":dict1["main"]["temp"],
    #         "desc":dict1["weather"][0]["description"],
    #         "icon":dict1["weather"][0]["icon"]
    #         }
    #     weather_app.append(my_dict)
    #     print(weather_app)
    #     my_weather={"weather_app":weather_app}
    # return render(request, "weatherApp/index.html",context=my_weather)

    #here for the get reequest
    form=forms.WeatherForm()
    if request.method=="POST":
        form=forms.WeatherForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            name=form.cleaned_data["name"]
            key="667fea17e45960efd542e3fdfc3dd9d6"
            url=f"https://api.openweathermap.org/data/2.5/weather?q={name}&units=metric&appid={key}"
            resp=requests.get(url)
            dict1=resp.json()#fetching the python dictionary from the url
            my_weather={
            "name":dict1["name"],
            "temp":dict1["main"]["temp"],
            "desc":dict1["weather"][0]["description"],
            "icon":dict1["weather"][0]["icon"]
            }
            return render(request, "weatherApp/index.html", {"form":form,"my_weather":my_weather})
    if request.method=="GET":
        form=forms.WeatherForm()
    return render(request, "weatherApp/index.html", {"form":form})

