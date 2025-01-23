# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:20:22 2023

@author: Anwesha Sarangi
"""

#Import libraries
import cv2 as cv
import numpy as np
import pyttsx3
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice rate (default is 200)
engine.setProperty('rate', 180)

# Set the voice volume (default is 1)
engine.setProperty('volume', 1)

#Load face cascade and hair cascade from haarcascades folder
face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_eye.xml')

#Capture video from webcam
video_capture = cv.VideoCapture(0)

#Read all frames from webcam
while True:
    ret, frame = video_capture.read()
    frame = cv.flip(frame,1) #Flip so that video feed is not flipped, and appears mirror like.
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)==0:
        print("no eyes detected")
        def alert(message):
            engine.say(message)
            engine.runAndWait()

        # Example usage
        winsound.Beep(frequency, duration)
        alert("Attention! NO FACE OR EYES DETECTED !!! driver is drowsy   STOP DRIVING.")

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
     
        

    cv.imshow('Video', frame)

    if(cv.waitKey(1) & 0xFF == ord('q')):
        break
import yawn_alert #runs yawn_alert.py script
#Gives the finial output
video_capture.release()
cv.destroyAllWindows()