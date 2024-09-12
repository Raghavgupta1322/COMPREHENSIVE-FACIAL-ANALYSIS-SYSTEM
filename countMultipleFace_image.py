# import linrary
import cv2
import os
face_cascade = cv2.CascadeClassifier('Input/haarcascade_frontalface_default.xml')

# list of images
images = ['1.jpg','1p.jpg','3p.jpg','7p.jpg','7pp.jpg','group.jpg']
count = 0
for i in images:
    img = cv2.imread(i)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.29, 4)

    for (x, y, w, h) in faces:
        # draw rectangale around face
        img = cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),2)
        # draw circle around face
        # img = cv2.circle(img, (x + int(w/2), y + int(h/2.4)),int(2*w/3.2), (0,255,0), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "FACE COUNTED : " + str(len(faces)),(10, 50), font, 1, (0, 0, 255),2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
cv2.waitKey(500)
os.system("python home.py")