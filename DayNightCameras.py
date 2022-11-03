#!/usr/bin/env python3
# importing necessary packages
import numpy as np
import cv2
from imutils.video import VideoStream
import time
from datetime import datetime
import os
import random
import sys

# setting frame rate and video resolution
fps = 24
width = 864
height = 640
video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

# setting folder name
name = datetime.now()
name = os.path.join(os.getcwd(), str(name))
print("ALl logs saved in dir:", name)
os.mkdir(name)

# night vision camera 
cap = cv2.VideoCapture(0)
ret = cap.set(3, 864)
ret = cap.set(4, 480)
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# webcam
webcam = cv2.VideoCapture(1)
webret = cap.set(3, 864)
webret = cap.set(4, 480)
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


# initialisation
start = time.time()
video_file_count = 1
DV_video_file = os.path.join(name, "DV_" + str(video_file_count) + ".avi")
NV_video_file = os.path.join(name, "NV_" + str(video_file_count) + ".avi")

# Create a video write before entering the loop
DV_video_writer = cv2.VideoWriter(
    DV_video_file, video_codec, fps, (int(webcam.get(3)), int(webcam.get(4)))
)
NV_video_writer = cv2.VideoWriter(
                NV_video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
)

while cap.isOpened():
    start_time = time.time()
    ret, frame = cap.read()
    webret, webframe = webcam.read()
    if ret == True:
        if time.time() - start > 60:
            start = time.time()
            video_file_count += 1
            DV_video_file = os.path.join(name, "DV_" + str(video_file_count) + ".avi")
            DV_video_writer = cv2.VideoWriter(
                DV_video_file, video_codec, fps, (int(webcam.get(3)), int(webcam.get(4)))
            )
            NV_video_file = os.path.join(name, "NV_" + str(video_file_count) + ".avi")
            NV_video_writer = cv2.VideoWriter(
                NV_video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
            )
            # No sleeping! We don't want to sleep, we want to write
            # time.sleep(10)

        # Write the frame to the current video writer
        DV_video_writer.write(webframe)
        NV_video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
webcam.release()

cv2.destroyAllWindows()