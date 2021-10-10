from django.shortcuts import render

# Create your views here.
def set_session(request):
    count=request.session.get("count",default=0)
    newcount=count+1
    request.session["count"]=newcount #adding the New count value to the count value
    return render(request, "fileBasedSessionApp/setsession.html", {"count":newcount})
    #rendering with the New count value with file Base Session Framework

def delete_session(request):
    request.session.flush()
    # request.session.clear_expired()
    return render(request, "fileBasedSessionApp/setsession.html")
