from django.shortcuts import render

# Create your views here.
#imp:-remeber all the value send as cookie value is in the str format so don't forget to typecast it
def index_view(request):#view function with request object
    count=int(request.COOKIES.get("count",0))#fetcghing the cookie from the reqeuest
    #all the value to the copokie be in the string format type cast to int in order to add
    new_count=count+1#incrementing the cookie value
    resp=render(request, "cookieApp/index.html", {"count":new_count})
    #creating the response object in order to set the cookie
    #also to render the cookie value
    resp.set_cookie("count",new_count)#setting the cooking value to the server
    #this value goes like a string to the cookiw
    #here we will be sending the cooking from server and maintained by the client
    return resp#returning the response object
