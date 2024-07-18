from django.shortcuts import render, redirect
from .models import Registraion
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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User = get_user_model()
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect(Home)
    template = 'auth.html'
    return render(request, template)