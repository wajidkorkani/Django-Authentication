from django.shortcuts import render

# Create your views here.

def Home(request):
    template = 'index.html'
    context = {
        'Text' : 'Hello django!'
    }
    return render(request, template, context)
