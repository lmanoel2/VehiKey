from django.shortcuts import render
from django.http import HttpResponse
def camera(request):
    return HttpResponse('Estou em /camera')