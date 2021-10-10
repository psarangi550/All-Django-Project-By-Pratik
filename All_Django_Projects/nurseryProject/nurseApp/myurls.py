from django.conf.urls import url
from django.urls import path
from Django_Durga.All_Django_Projects.nurseryProject.nurseApp import views
urlpatterns = [
    url(r"^$",views.temp_view)
]