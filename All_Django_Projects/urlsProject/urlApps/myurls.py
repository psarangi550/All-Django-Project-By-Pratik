from django.conf.urls import url
from Django_Durga.All_Django_Projects.urlsProject.urlApps import views
from django.urls import path
from django.contrib import admin
#importing the url function
urlpatterns = [
    # path("admin/",admin.site.urls),
    path("hyd/", views.hyd_jobs_urls),
    url(r"^punejobs/",views.pune_jobs_urls),
    url(r"^mumbaijobs/",views.mumbai_jobs_urls)
]