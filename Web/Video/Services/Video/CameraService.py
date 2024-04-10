import cv2
import threading
import numpy as np
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
            self.activated = False
            return

        self.set_frame()
        threading.Thread(target=self.update, args=()).start()

    def update(self):
        while self.activated:
            if self.is_timeout_response_web():
                self.video.release()

            self.set_frame()

    def change_to_camera(self, camera):
        print('change_camera_to_camera')
        # self.changed_cam = False
        # self.video = cv2.VideoCapture(0)

    def set_frame(self):
        (_, self.frame) = self.video.read()

    def get_bytes_image(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_video(self):
        while self.activated:
            bytes_image = self.get_bytes_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + bytes_image + b'\r\n\r\n')

    def is_timeout_response_web(self):
        return (datetime.now(timezone.utc) - self.last_keep_alive).seconds > 0.01

    def get_black_image(self):
        black_image = np.zeros((600, 600, 3), dtype=np.uint8)
        return black_image
