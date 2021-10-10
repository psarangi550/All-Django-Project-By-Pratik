from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.index_view),
    path('thankyou/', views.thank_view)
]
