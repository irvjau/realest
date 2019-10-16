
from django.conf.urls import url
from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', views.home),    #properties home page
    path('properties/prop', prop_page),    #properties page

]