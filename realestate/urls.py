"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from .views import *
from properties.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_page),                       # homepage 
    #path('', base_page),                       # intro 
    #path('home/', home_page),                    # home
    path('admin/', admin.site.urls),            # admin page 
    path('about/', about_page),                 # about page
    path('example/', example_page),             # example page 
    path('contact/', contact_page),             # contact page
    path('signup/', signup_page),               # signup page
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),     #login page
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),     #logout page
    path('buy/', buy_page),                     # buy page
    path('sell/', sell_page),                   # sell page  
    path('buy/prop/<slug:address>', prop_page), #individual url for each property
    path('properties/', include('properties.urls')),  # link properties urls
    path('accounts/', include('accounts.urls')),  # link account urls
]


urlpatterns += staticfiles_urlpatterns()
