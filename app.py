#!/usr/bin/python
import argparse


from time_lapse import TimeLapseCamera

if __name__ == '__main__':
    #parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--camera_port', type=int,   default=0,      help='The index of the camera.')
    parser.add_argument('-c', '--codec',       type=str,   default='mp4v', help='4 bit codec')
    parser.add_argument('-l', '--time_limit',  type=float, default=5*60.,  help='Set a time limit in seconds.')
    parser.add_argument('-t', '--output_time', type=float, default=15.,    help='Set a result video time in seconds.')
    parser.add_argument('-f', '--fps',         type=int,   default=30,     help='Frames per second.')
    parser.add_argument('-i', '--interval',    type=float, default=1.,     help='Time in seconds between shoots.')
    args = parser.parse_args()

    camera = TimeLapseCamera(camera_port=args.camera_port,
                             codec_name=args.codec,
                             fps=args.fps,
                             time_limit=args.time_limit,
                             output_time=args.output_time,
                             interval=args.interval)
    camera.start()
    camera.release()