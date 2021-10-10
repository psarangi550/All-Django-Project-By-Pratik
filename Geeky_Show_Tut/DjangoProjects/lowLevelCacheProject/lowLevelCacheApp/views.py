from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
# def home_view(request):
#     mv=cache.get("movie",default="expired")
#     if mv=="expired":
#         cache.set("movie","The Ctea",timeout=60)
#         mv=cache.get("movie")
#     return render (request, "lowLevelCacheApp/index.html", {"mv":mv})

# def home_view(request):
#     cache.add(key="mark",value=105,timeout=60,version=1)
#     nm=cache.get_or_set(key="mark",default=0,version=1)
#     return render (request, "lowLevelCacheApp/index.html", {"mv":nm})

# def home_view(request):
#     dict1={"name":"rika","roll":1113,"mark":90}
#     # cache.set_many(dict1,timeout=60)
#     dict=cache.get_many(dict1)
#     return render (request, "lowLevelCacheApp/index.html", {"mv":dict})

# def index_view(request):
#     dict=cache.get_or_set("fruit",900,30)
#     return render (request, "lowLevelCacheApp/index.html", {"mv":dict})

# def home_view(request):
#     # cache.clear()
#     cache.delete("movie")
#     # val=cache.get("movie")
#     # print(val)
#     return render (request, "lowLevelCacheApp/index.html")


def home_view(request):
    cache.set("count",100,timeout=60)
    mv=cache.incr("count",delta=1)
    # mv=cache.get("movie")
    print(mv)
    request.session.modified=False
    return render (request, "lowLevelCacheApp/index.html", {"mv":mv})
