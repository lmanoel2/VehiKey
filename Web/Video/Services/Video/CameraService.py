import cv2
import threading
import numpy as np
import ast
from datetime import datetime, timezone


class CameraService(object):
    activated = True
    not_found_video = False

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
            if self.is_timeout_response_web() and self.video:
                self.video.release()

            self.set_frame()

    def change_to_camera(self, camera):
        camera_dict = ast.literal_eval(camera)
        #'admin','admin123','10.0.0.106'
        #rtspUrl = f'rtsp://{camera_dict['user']}:{camera_dict['password']}@{camera_dict['ip']}:554/cam/realmonitor?channel=1&subtype=0'
        #TODO: RETIRAR CONSTANTE QUE FUNFA
        rtspUrl = f'rtsp://admin:admin123@10.0.0.106:554/cam/realmonitor?channel=1&subtype=0'
        print(rtspUrl)
        cap = cv2.VideoCapture(rtspUrl)

        if not cap.isOpened():
            print(f"Unable to connect to camera")
            self.not_found_video = True
            return

        self.video = cap
        self.set_frame()

    def get_video(self):
        while self.activated:
            bytes_image = self.get_bytes_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + bytes_image + b'\r\n\r\n')

    def get_bytes_image(self):
        if self.frame is not None and self.frame.size > 0:
            image = self.frame
        else:
            image = self.get_black_image()

        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def is_timeout_response_web(self):
        return (datetime.now(timezone.utc) - self.last_keep_alive).seconds > 0.01

    def set_frame(self):
        if not self.video:
            self.frame = None
        else:
            (_, self.frame) = self.video.read()

    def get_black_image(self):
        black_image = np.zeros((600, 600, 3), dtype=np.uint8)
        return black_image
