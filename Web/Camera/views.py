from django.shortcuts import render
from django.http import HttpResponse
import os, sys
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from Domain.Model.CameraModel import CameraModel


def camera(request):
    if request.method == 'GET':
        return render(request, 'camera.html')
    if request.method == 'POST':
        names = request.POST.getlist('name')
        ips = request.POST.getlist('ip')
        ports = request.POST.getlist('port')
        url = 'http://127.0.0.1:5000/camera'

        # camera = CameraModel(name=names, ip=ips, port=ports)
        for name, ip, port in zip(names, ips, ports):
            model = CameraModel(name=name,
                                ip=ip,
                                port=port,
                                user='admin',
                                password='admin123',
                                manufacturer='INTELBRAS')
            data = dict(model)
            requests.post(url, json=data)

        return HttpResponse(names)
