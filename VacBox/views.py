# Create your views here.

from django.shortcuts import render

def vacBox(request):
    return render(request, 'index.html')

def notFound(request):
    return render(request, '404.html')