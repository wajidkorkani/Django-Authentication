from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
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
        "form":RegistrationForm(request.POST)
    }
    return render(request, template, context)

def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(Home)
        else:
            template = 'login.html'
            context = {
                'error' : 'Invalid useranme or password!'
            }
            return render(request, template, context)
    
    template = 'login.html'
    return render(request, template)
