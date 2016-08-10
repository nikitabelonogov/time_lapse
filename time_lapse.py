#!/usr/bin/python
import cv2


class TimeLapseCamera:
    def __init__(self, camera_port=-1, codec_name='mp4v', fps=60, time_limit=15, output_time=15, interval=1):
        print('Camera initialization.')
        self.camera = cv2.VideoCapture(camera_port)
        self.fourcc = cv2.cv.CV_FOURCC(*codec_name)
        width = int(self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        height = int(self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.video = cv2.VideoWriter('video.mp4', self.fourcc, fps, (width, height))
        self.interval = time_limit / (output_time * fps)

    def shoot(self):
        _, camera_capture = self.camera.read()
        self.video.write(camera_capture)
        cv2.imshow('Video', camera_capture)

    def release(self):
        self.video.release()

    def start(self):
        while True:
            self.shoot()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
