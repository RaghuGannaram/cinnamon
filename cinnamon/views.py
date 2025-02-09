from django.http import HttpResponse
from django.shortcuts import render

def health_check(request):
    return HttpResponse('OK')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# 


