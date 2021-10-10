from django.shortcuts import render

def display_view(request):
    age=request.POST.get("age")
    resp=render(request, "cookieApp/display.html", {"count":request.COOKIES.get("id"), "name":request.COOKIES.get("name"),"age":request.POST.get("age")})
    resp.set_cookie("age",age)
    return resp
def age_views(request):
    name=request.GET.get("name")
    if request.method=="POST":
        name=request.POST.get("name")
        resp=render(request, "cookieApp/age.html",{"count":request.COOKIES.get("id"),"name":name})
        resp.set_cookie("name",name)
        return resp
    render(request, "cookieApp/age.html",{"count":request.COOKIES.get("id"),"name":name})

def name_view(request):
    id=request.GET.get("id")
    if request.method=="POST":
        id=request.POST.get("id")
        resp=render(request, "cookieApp/name.html",{"id":id})
        resp.set_cookie("id",id)
        return resp
    return render(request, "cookieApp/name.html", {"id":id})
def index_view(request):
    if request.method=="POST":
        render(request, "cookieApp/name.html")
    return render(request, "cookieApp/index.html")
