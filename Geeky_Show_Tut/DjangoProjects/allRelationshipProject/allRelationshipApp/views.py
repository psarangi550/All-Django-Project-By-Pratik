from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Song,Page,Post
from datetime import date
# Create your views here.
#defining the view function with the queries
#rememebr that when we are queryibng inside the model we can query by field__lookupfield=value
#remeber that when we query using the another model field we can query by using the <model>__field__lookupfield=value

#deining the home page view
def index_view(request):
    return render(request, "allRelationshipApp/index.html",)


#deining the views for the one to one table
def show_user_data(request):
    data1=User.objects.all()
    data2=User.objects.filter(page__page_cat__startswith="plan")
    data3=User.objects.filter(post__post_name__icontains="EC2")
    data4=User.objects.filter(song__song_name__iexact="Hurt")
    return render(request, "allRelationshipApp/user.html", {"data1":data1,"data2":data2,"data3":data3,"data4":data4})

#displaying the result as Per the Page Information
def show_page_details(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(user__post__post_name="Read Django Rest Frameworks")
    data3=Page.objects.filter(user__song__song_name="Hurt")
    data4=Page.objects.filter(user__username__startswith="a")
    return render(request, "allRelationshipApp/page.html", {"data1":data1,"data2":data2,"data3":data3,"data4":data4})

#displaying all the post_related info using the query by filter
def show_post_details(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(user__page__page_cat="Programming")
    data3=Post.objects.filter(user__song__song_name="Hurt").order_by("id")
    data4=Post.objects.filter(post_date=date(2021,10,12)).order_by("id")
    return render(request, "allRelationshipApp/post.html", {"data1":data1,"data2":data2,"data3":data3,"data4":data4})

#defining the Queries for the many to many fields

def show_song_details(request):
    data1=Song.objects.all()
    data2=Song.objects.filter(user__page__page_cat="Programming")
    data3=Song.objects.filter(user__post__post_date=date(2021,9,15))
    data4=Song.objects.filter(song_name__istartswith="l")
    return render(request, "allRelationshipApp/songs.html", {"data1":data1,"data2":data2,"data3":data3,"data4":data4})
