from django.urls import path #importing the path function from urls modules
from . import views
urlpatterns=[
    path("django/",views.django_view,name="django")
]