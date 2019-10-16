from django.shortcuts import render, HttpResponse
from django.utils.text import slugify
from properties.models import *
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, "properties.html")

def prop_page(request, address):
    newAddress = address.replace('-',' ')
    newAddress = newAddress.upper()

    property = Properties.objects.get(street=newAddress)    #retrieve object with address passed to webpage
    
    context = {
        "property" : property,
        "address": newAddress,
    }

    return render(request, "properties.html", context)
