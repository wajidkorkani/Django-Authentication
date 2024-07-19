from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import get_user_model
# Create your views here.

def Home(request):
    template = 'index.html'
    context = {
        'Text' : 'Hello django!'
    }
    return render(request, template, context)

def UserRegistration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegistrationForm(request.POST)
    template = 'auth.html'
    context = {
        "form":form
    }
    return render(request, template, context)
