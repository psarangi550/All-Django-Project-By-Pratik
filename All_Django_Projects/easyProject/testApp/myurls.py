from django.conf.urls import url
from django.urls import path
from Django_Durga.All_Django_Projects.easyProject.testApp import views
urlpatterns = [
    url(r"^test/",views.temp_view)
]