from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'optifolio/dashboard.html')

def visualization(request):
    return render(request, 'optifolio/visualization.html')

def optimalization(request):
    return render(request, 'optifolio/optimalization.html')




