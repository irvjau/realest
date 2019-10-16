
from django.conf.urls import url
from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url('', views.home),
    path('signup/', signup_page),               # signup page
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),     #login page
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),     #logout page

]