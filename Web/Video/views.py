import json
from datetime import datetime, timezone
from django.views.decorators import gzip
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from django.middleware.csrf import get_token

from Web.Endpoints.CameraEndpoints import CameraEndpoints
from Web.Endpoints.ControlsEndpoints import ControlsEndpoints
from Web.Video.Services.Video.CameraService import CameraService

cameraService = CameraService()
cameraEndpoints = CameraEndpoints()
controlsEndpoints = ControlsEndpoints()
cameras = cameraEndpoints.GetAllCameras()

def video(request):
    if request.method == 'GET':
        cameraService.activated = False
        return render(request, 'video.html', {'cameras': cameras, 'csrf_token': get_token(request)})
    if request.method == 'POST':
        cameraService.activated = False
        return render(request, 'video.html', {'cameras': cameras})

def keep_alive(request):
    cameraService.last_keep_alive = datetime.now(timezone.utc)
    return JsonResponse({'status': 'ok'})

def changed_cam(request):
    camera = request.POST.get('camera')
    cameraService.change_to_camera(camera)
    return JsonResponse({'status': 'ok'})

@gzip.gzip_page
def stream(request):
    camera = request.POST.get('camera')
    cameraService.start()
    return StreamingHttpResponse(cameraService.get_video(), content_type="multipart/x-mixed-replace;boundary=frame")

def send_command(request):
    control = request.POST.get('control')
    control_json = json.loads(control)
    controlsEndpoints.SendCommand(control_json)
    return JsonResponse('ok', safe=False)