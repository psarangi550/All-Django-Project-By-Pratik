from django.urls import path
from . import views
urlpattern=[
    path("index/",views.index_view),
    path("thanks/",views.thanks_view)
]