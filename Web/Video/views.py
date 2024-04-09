import cv2
import threading
from datetime import datetime, timezone
from django.views.decorators import gzip
from django.http import StreamingHttpResponse, HttpResponse, JsonResponse
from django.shortcuts import render


last_keep_alive = datetime.now(timezone.utc)
activated = True

def video(request):
    if request.method == 'GET':
        global activated
        activated = False
        return render(request, 'video.html')

def keep_alive(request):
    global last_keep_alive
    last_keep_alive = datetime.now(timezone.utc)
    return JsonResponse({'status': 'ok'})

@gzip.gzip_page
def stream(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return HttpResponse("Video acessado com sucesso")


# to capture video class
class VideoCamera(object):
    def __init__(self):
        global last_keep_alive
        global activated
        activated = True
        self.video = cv2.VideoCapture(0)

        if not self.video.isOpened():
            print(f"Unable to connect to camera")
            activated = False
            return

        (_, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        last_keep_alive = datetime.now(timezone.utc)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        global activated
        global last_keep_alive

        while activated:

            if (datetime.now(timezone.utc) - last_keep_alive).seconds > 0.01:
                self.video.release()
                activated = False
            (_, self.frame) = self.video.read()


def gen(camera):
    global activated
    while activated:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
