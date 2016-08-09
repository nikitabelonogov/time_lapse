#!/usr/bin/python
import cv2
import argparse
import threading


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--camera_port', type=int, default=-1,     help='The index of the camera.')
parser.add_argument('-c', '--codec',       type=str, default='mp4v', help='4 bit codec')
parser.add_argument('-l', '--time_limit',  type=int,                 help='Set a time limit in seconds.')
parser.add_argument('-t', '--output_time', type=int,                 help='Set a result video time in seconds.')
parser.add_argument('-f', '--fps',         type=int, default=60,     help='Frames per second.')
parser.add_argument('-i', '--interval',    type=int,                 help='Time in seconds between shoots.')
args = parser.parse_args()


class TimeLapseCamera:
    def __init__(self, camera_port=0, codec_name='mp4v', fps=60):
        print('Camera initialization.')
        self.camera = cv2.VideoCapture(camera_port)
        self.fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
        self.fourcc = cv2.cv.CV_FOURCC(*codec_name)
        width = int(self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        height = int(self.camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.video = cv2.VideoWriter('video.mp4', self.fourcc, fps, (width, height))

    def shoot(self):
        _, camera_capture = self.camera.read()
        self.video.write(camera_capture)

    def release(self):
        self.video.release()

if __name__ == '__main__':
    camera = TimeLapseCamera(camera_port=args.camera_port, codec_name=args.codec, fps=args.fps)
    for _ in range(60):
        camera.shoot()
    camera.release()
