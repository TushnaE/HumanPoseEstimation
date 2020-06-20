# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np
import torch
import time

from src import model
from src import util
from src.body import Body

body_estimation = Body('model/body_pose_model.pth')

# cap = cv2.VideoCapture(0)
## AVI files are the only ones that can be opened w VideoCapture
cap = cv2.VideoCapture('images/babyjump.avi')
fourcc = cv2.VideoWriter_fourcc(*'MJPG') ## maybe try one that works best w OSX
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
cap.set(3, 640)
cap.set(4, 480)

frame = 0
print(frame)

# get the frame, do time.pause or smthg similar for right after frame

time_start = time.time()    #0
loop_time = time.time() + 2     #0

while (cap.isOpened()):
    ret, oriImg = cap.read()
    
    if (loop_time-time_start >= .4):             # time_start = 0
        print(loop_time-time_start)             # loop_time = 2

        candidate, subset = body_estimation(oriImg)
        canvas = copy.deepcopy(oriImg)
        canvas = util.draw_bodypose(canvas, candidate, subset)

        print("a new pose applied")
        cv2.imshow('demo', canvas)
        
        time_start = time.time()                  # time_start = 0
    loop_time = time.time()

    # cv2.imshow('demo', canvas)

    frame = frame +1
    print(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

