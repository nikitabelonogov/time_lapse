#!/usr/bin/python
import threading

import cv2
import time


class TimeLapseCamera:
    def __init__(self, camera_port=-1, codec='mp4v', fps=30, time_limit=60, output_time=15, interval=1):
        print('Camera initialization.')
        self.camera = cv2.VideoCapture(camera_port)
        self.fourcc = cv2.cv.CV_FOURCC(*codec)
        width = int(self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        height = int(self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.video = cv2.VideoWriter('video.mp4', self.fourcc, fps, (width, height))
        self.interval = time_limit / (output_time * fps)
        self.time_limit = time_limit

    def shoot(self):
        _, camera_capture = self.camera.read()
        self.video.write(camera_capture)
        cv2.imshow('Video', camera_capture)

    def release(self):
        self.video.release()

    def start(self):
        start_time = time.time()

        while start_time + self.time_limit >= time.time():
            self.shoot()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(1. / 30.)
