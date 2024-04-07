import os
import sys

from django.http import JsonResponse
from django.shortcuts import render

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from Web.Endpoints.CameraEndpoints import CameraEndpoints

cameraEndpoints = CameraEndpoints()


def camera(request):
    if request.method == 'GET':
        cameras = cameraEndpoints.GetAllCameras()
        return render(request, 'camera.html', {'cameras': cameras})
    if request.method == 'POST':
        cameraEndpoints.AddRange(request)
        cameras = cameraEndpoints.GetAllCameras()
        return render(request, 'camera.html', {'cameras': cameras})


def get_camera(request):
    cam_id = request.POST.get('id_camera')
    cam = cameraEndpoints.GetCameraById(cam_id)
    return JsonResponse(cam)

def update_camera(request):
    cam_id = request.POST.get('id_camera')
    cam = cameraEndpoints.GetCameraById(cam_id)
    return JsonResponse(cam)
