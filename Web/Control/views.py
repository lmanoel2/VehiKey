import os
import sys

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.middleware.csrf import get_token

from Web.Endpoints.ControlsEndpoints import ControlsEndpoints

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from Web.Endpoints.CameraEndpoints import CameraEndpoints

cameraEndpoints = CameraEndpoints()
controlsEndpoints = ControlsEndpoints()


def control(request):
    if request.method == 'GET':
        cameras = cameraEndpoints.GetAllCameras()
        return render(request, 'control.html', {'cameras': cameras, 'csrf_token': get_token(request)})
    if request.method == 'POST':
        cameraEndpoints.AddRange(request)
        cameras = cameraEndpoints.GetAllCameras()
        return render(request, 'control.html', {'cameras': cameras})

def send_command(request):
    action = request.POST.get('action')
    controlsEndpoints.SendCommand(action)
    return JsonResponse('ok', safe=False)