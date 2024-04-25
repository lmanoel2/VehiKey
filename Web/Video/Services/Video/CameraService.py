import cv2
import threading
import ast
from datetime import datetime, timezone


class CameraService(object):
    activated = True
    not_found_video = False
    changing_camera = False
    capture = None
    reading = False
    connecting = False
    video = None
    frame = None

    def __init__(self):
        self.can_get_true_image = None
        self.last_keep_alive = datetime.now(timezone.utc)

    def start(self):
        self.can_get_true_image = False
        self.activated = True
        self.not_found_video = True

    def update(self, video):
        while not self.changing_camera:
            if video is None:
                continue

            if self.is_timeout_response_web() and video:
                video.release()

            if not self.changing_camera:
                self.set_frame(video)

    def change_to_camera(self, camera):
        camera_dict = ast.literal_eval(camera)
        rtspUrl = f'rtsp://{camera_dict['user']}:{camera_dict['password']}@{camera_dict['ip']}:554/cam/realmonitor?channel=1&subtype=0'
        print(rtspUrl)
        self.changing_camera = True

        while self.reading or self.connecting:
            return

        self.connecting = True

        print('$$$$$$$$$$TRY open video')
        # thread = threading.Thread(target=self.open_video, args=(rtspUrl,))
        # thread.start()
        # thread.run(timeout=2.5)

        cap = self.open_video(rtspUrl)

        print('!!!!!!!!!!FINISH open video')

        if not cap or not cap.isOpened():
            self.not_found_video = True
            self.connecting = False
            self.can_get_true_image = False

            print(f"Unable to connect to camera")
            return

        print('!!!!!!!!!!opening')
        self.capture = None
        self.set_frame(cap)
        self.changing_camera = False
        self.not_found_video = False
        self.can_get_true_image = True
        self.connecting = False
        threading.Thread(target=self.update, args=(cap,)).start()

    def open_video(self, url):
        cap = cv2.VideoCapture(url)
        return cap

    def get_video(self):
        while self.activated:
            bytes_image = self.get_bytes_image()
            if bytes_image:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + bytes_image + b'\r\n\r\n')

    def get_bytes_image(self):
        if self.can_get_true_image and self.frame is not None:
            image = self.frame
            _, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()

    def can_get_true_image(self):
        return (not self.not_found_video and
                self.frame is not None and
                self.frame.size > 0)

    def is_timeout_response_web(self):
        return (datetime.now(timezone.utc) - self.last_keep_alive).seconds > 0.01

    def set_frame(self, video):
        if not self.not_found_video:
            if self.changing_camera:
                return

            self.reading = True
            (_, self.frame) = video.read()
            self.reading = False

    def set_not_found_video_to_false(self):
        self.not_found_video = False
