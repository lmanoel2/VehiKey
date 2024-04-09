import cv2
import threading
from datetime import datetime, timezone


class CameraService(object):
    activated = True

    def __init__(self):
        self.last_keep_alive = datetime.now(timezone.utc)

    def __del__(self):
        self.video.release()

    def start(self):
        self.activated = True
        self.video = cv2.VideoCapture(0)

        if not self.video.isOpened():
            print(f"Unable to connect to camera")
            activated = False
            return

        (_, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        last_keep_alive = datetime.now(timezone.utc)

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while self.activated:

            if (datetime.now(timezone.utc) - self.last_keep_alive).seconds > 0.01:
                self.video.release()
                activated = False
            (_, self.frame) = self.video.read()

    def get_video(self):
        while self.activated:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
