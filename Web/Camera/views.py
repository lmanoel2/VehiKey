from django.shortcuts import render
from django.http import HttpResponse

def camera(request):
    return render(request, 'camera.html')