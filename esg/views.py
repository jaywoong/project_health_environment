from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def health(request):
    return render(request, 'health.html')

def environment(request):
    return render(request, 'environment.html')

def corr(request):
    return render(request, 'corr.html')

def use(request):
    return render(request, 'use.html')