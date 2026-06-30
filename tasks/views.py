from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the Tasks Homepage</h1><p>Your to-do list foundation.</p>")

def about(request):
    return HttpResponse("<h1>About This App</h1><p>This is a Django tasks app built for managing daily to-dos.</p>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>Get in touch at admin@example.com</p>")