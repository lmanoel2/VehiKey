import os
import sys

import requests
from django.http import JsonResponse
from django.shortcuts import render

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from Web.Endpoints.CameraEndpoints import CameraEndpoints
from Domain.Model.CameraModel import CameraModel

cameraEndpoints = CameraEndpoints()


def camera(request):
    if request.method == 'GET':
        cameras = cameraEndpoints.GetAllCameras()
        return render(request, 'camera.html', {'cameras': cameras})
    if request.method == 'POST':
        names = request.POST.getlist('name')
        ips = request.POST.getlist('ip')
        ports = request.POST.getlist('port')
        url = 'http://127.0.0.1:5000/camera'

        for name, ip, port in zip(names, ips, ports):
            model = CameraModel(name=name,
                                ip=ip,
                                port=port,
                                user='admin',
                                password='admin123',
                                manufacturer='INTELBRAS')
            data = dict(model)
            requests.post(url, json=data)

        return render(request, 'camera.html', {'cameras': zip(names, ips, ports)})


def get_camera(request):
    cam_id = request.POST.get('id_camera')
    cam = cameraEndpoints.GetCameraById(cam_id)
    return JsonResponse(cam)

def update_camera(request):
    cam_id = request.POST.get('id_camera')
    cam = cameraEndpoints.GetCameraById(cam_id)
    return JsonResponse(cam)
