import cv2
import threading
import numpy as np
import ast
from datetime import datetime, timezone


class CameraService(object):
    activated = True
    not_found_video = False
    changing_camera = False
    capture = None
    reading = False
    connecting = False

    def __init__(self):
        self.last_keep_alive = datetime.now(timezone.utc)

    def start(self):
        self.activated = True
        rtsp_url = 'rtsp://admin:admin123@10.0.0.106:554/cam/realmonitor?channel=1&subtype=0'

        self.video = cv2.VideoCapture(rtsp_url)

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

            if not self.changing_camera:
                self.set_frame()

    def change_to_camera(self, camera):
        camera_dict = ast.literal_eval(camera)
        rtspUrl = f'rtsp://{camera_dict['user']}:{camera_dict['password']}@{camera_dict['ip']}:554/cam/realmonitor?channel=1&subtype=0'
        print(rtspUrl)
        self.changing_camera = True

        while self.reading or self.connecting:
            pass

        self.connecting = True


        print('$$$$$$$$$$TRY open video')
        thread = threading.Thread(target=self.open_video, args=(rtspUrl,))
        thread.start()
        thread.join(timeout=2.5)
        print('!!!!!!!!!!FINISH open video')

        if not self.video or not self.video.isOpened():
            self.not_found_video = True
            self.connecting = False
            print(f"Unable to connect to camera")
            return


        # self.video = self.capture
        self.capture = None
        self.set_frame()
        self.changing_camera = False
        self.not_found_video = False
        self.connecting = False

    def open_video(self, url):
        self.video = cv2.VideoCapture(url)

    def get_video(self):
        while self.activated:
            bytes_image = self.get_bytes_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + bytes_image + b'\r\n\r\n')

    def get_bytes_image(self):
        if self.can_get_true_image():
            image = self.frame
        else:
            image = self.get_black_image()

        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def can_get_true_image(self):
        return (not self.not_found_video and
                self.frame is not None and
                self.frame.size > 0)

    def is_timeout_response_web(self):
        return (datetime.now(timezone.utc) - self.last_keep_alive).seconds > 0.01

    def set_frame(self):
        if self.not_found_video or not self.video:
            return
            #self.frame = self.get_black_image()
        else:
            if self.changing_camera:
                return

            self.reading = True
            (_, self.frame) = self.video.read()
            self.reading = False

    def set_not_found_video_to_false(self):
        self.not_found_video = False

    def get_black_image(self):
        black_image = np.zeros((600, 600, 3), dtype=np.uint8)
        return black_image
