from django.urls import path
from . import views
#importing the path function form  django module
urlpatterns=[
    path("thankyou/",views.thankyou_view),
    path("",views.feedback_view)
]
