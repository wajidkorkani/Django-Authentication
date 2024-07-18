from django.shortcuts import render
from .models import Registraion
# Create your views here.

def Home(request):
    template = 'index.html'
    context = {
        'Text' : 'Hello django!'
    }
    return render(request, template, context)

def UserRegistration(request):
    template = 'auth.html'
    return render(request, template)