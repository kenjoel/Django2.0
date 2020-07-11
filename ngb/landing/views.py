from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

products = [
    {
        'name':'Serial code scanner',
        'description':'This is a Kenyan made scanner. It is useful in commerce',
        'price':4300

    },
    {
        'name':'Mathelin Bags',
        'description':'These classic Khaki are examples of what quality is',
        'price':6000

    },
    {
        'name':'Banner remover',
        'description':'This is a cuban made banner remover. Its is used mainly for production',
        'price':7300

    }
]

def home(request):
    context = {
        'products':products
    }
    return render(request, 'landing/landing.html', context)

def about(request):
    return render(request, 'landing/about.html')

def login(request):
    return render(request, 'landing/login.html')