# import numpy as np
import cv2
import os
# classifiers
face_cascade = cv2.CascadeClassifier('Input/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Input/haarcascade_eye_tree_eyeglasses.xml')


# image read
fname = ['1p.JPG','2p.jpg','3p.jpg']
for i in fname:
    img = cv2.imread(i)
    cv2.namedWindow("Eye Detection")
    cv2.moveWindow("Eye Detection", 50, 0)
    cv2.imshow('Eye Detection',cv2.resize(img, (1000, 750)))
    cv2.waitKey(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.namedWindow("Eye Detection")
        cv2.moveWindow("Eye Detection", 50, 0)
        cv2.imshow('Eye Detection', cv2.resize(img, (1000, 750)))
        cv2.waitKey(0)
        # roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_color)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.namedWindow("Eye Detection")
        cv2.moveWindow("Eye Detection", 50, 0)
        cv2.imshow('Eye Detection',cv2.resize(img, (1000, 750)))
        cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(500)
os.system("python home.py")