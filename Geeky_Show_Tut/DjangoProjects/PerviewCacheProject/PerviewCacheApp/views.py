from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

#@cache_page(60)#here we are using the cache_page decorator with 60 sec as the time out
#another way to do it using the urls.py where we can render 2 different url one with cache other one without cahce
#check out the  urls.py for more instruction follow
def index_view(request):#view fuinction with index_view
    return render(request, "PerViewCacheApp/index.html")#rendering the index page
