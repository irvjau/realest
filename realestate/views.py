from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm
from properties.models import *
from django.db.models import Q
from django.core.paginator import Paginator

def home_page(request):
    my_title = "Welcome"        #string to pass
    return render(request, "home.html", {'title': "Welcome"})# , 'my_list': [1, 2, 3, 4, 5]})

def about_page(request):
    return render(request, "about.html", {'title': "About us"})

def contact_page(request):
    return render(request, "contact.html", {'title': "Contact us"})

def example_page(request):      # rendering the template in another context 
    context = {"title": "example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return Render(template_obj.render(context))

def intro_page(request):
    return render(request, "intro.html", {'title': "intro"})

def base_page(request):
    return render(request, "base.html")

def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
        else:
            print(form.errors)
    else:
        form = SignUpForm

    args = {'form': form}
    return render(request, 'signup_form.html', args)

def buy_page(request):
    queryset_list = Properties.objects.all()
    
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter( 
                Q(street__icontains=query) |
                Q(city__icontains=query) 
                ).distinct()    

    
    paginator = Paginator(queryset_list, 25)
    page = request.GET.get('page')
    properties = paginator.get_page(page)

    context = {
        "properties" : properties
    }

    return render(request, "buy.html", context)

def sell_page(request):
    return render(request, "sell.html")
    
    