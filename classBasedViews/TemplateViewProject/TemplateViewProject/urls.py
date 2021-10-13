"""TemplateViewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView #importing the template View
from TemplateViewApp2 import views
from TemplateViewApp3 import views as v3
from TemplateViewApp4 import views as v4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="TemplateViewApp/index.html"),name="index"),
    path('home/', views.MyTemplateView.as_view(),name="home"),
    path('display/', v3.MyTemplateContextView.as_view(extra_context={"course":"django"}),name="display"),
    path('dynamic/', v4.MyTemplateDynamicontextView.as_view(extra_context={"course":"django"}),name="dynamic123"),
    path('dynamic/<int:id>', v4.MyTemplateDynamicontextView.as_view(extra_context={"course":"django"}),name="dynamic"),
]
