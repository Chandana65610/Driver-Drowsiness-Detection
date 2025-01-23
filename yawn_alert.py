# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:22:25 2023

@author: Anwesha Sarangi
"""

import cv2
import numpy as np
import math
import pyttsx3
import winsound
import tkinter as tk
import webbrowser
import os


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice rate (default is 200)
engine.setProperty('rate', 180)

# Set the voice volume (default is 1)
engine.setProperty('volume', 1)
# Load the face and mouth cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

# Capture video from the camera
cap = cv2.VideoCapture(0)

# Initialize variables
yawn_count = 0
yawn_alert = False

# Loop over frames from the video stream
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Get the region of interest (ROI) which is the mouth area
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect mouths in the ROI
        mouths = mouth_cascade.detectMultiScale(roi_gray, 1.7, 11)

        # Check if there is at least one mouth
        
            
        if len(mouths) > 0:
            # Get the mouth with the largest area
            mouth = max(mouths, key=lambda x: (x[2] * x[3]))

            # Draw a rectangle around the mouth
            (mx, my, mw, mh) = mouth
            cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (255, 0, 0), 2)

            # Calculate the aspect ratio of the mouth
            ar = (mw / mh)

            # Check if the aspect ratio is below a threshold
            if ar < 0.5:
                # Increment the yawn count
                yawn_count += 1
                print("yawn detected")

                # Set the yawn alert flag
                yawn_alert = True
        if len(mouths) == 0:
            def alert(message):
                engine.say(message)
                engine.runAndWait()

            # Example usage
            winsound.Beep(frequency, duration)
            alert("Attention!DRIVER IS YAWNING")
            yawn_count = 0

    # Display the frame
    cv2.imshow('frame', frame)

    # Check if the yawn alert flag is set
    if yawn_alert:
        # Print a message and reset the yawn alert flag
        print('Yawn detected. Yawn count: {}'.format(yawn_count))
        yawn_alert = False

    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
import end