import cv2
import numpy as np
from PIL import Image 

# Get user supplied values

cascPath = ("haarcascade_frontalface_default.xml")

eyecascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

eyecascade = cv2.CascadeClassifier('eyecascade')

cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    
    cv2.imshow('gray', gray)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()



