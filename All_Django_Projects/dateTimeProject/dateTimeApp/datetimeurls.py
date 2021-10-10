from django.conf.urls import url
from Django_Durga.All_Django_Projects.dateTimeProject.dateTimeApp import views
urlpatterns = [
    url(r"^date/",views.welcome)
]