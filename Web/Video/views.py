import json
from datetime import datetime, timezone
from django.views.decorators import gzip
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render

from Web.Endpoints.CameraEndpoints import CameraEndpoints
from Web.Video.Services.Video.CameraService import CameraService

cameraService = CameraService()
cameraEndpoints = CameraEndpoints()
cameras = cameraEndpoints.GetAllCameras()

def video(request):
    if request.method == 'GET':
        cameraService.activated = False
        return render(request, 'video.html', {'cameras': cameras})
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
