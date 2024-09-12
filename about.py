#Import all the necessary libraries
import cv2
import os

path = "Input/img/about/a"
for i in range(1,26):
    img = cv2.imread(path+str(i)+".jpg")
    cv2.namedWindow("About")
    cv2.moveWindow("About",150,0)
    cv2.imshow('About', cv2.resize(img,(1200,750)))
    cv2.waitKey(500) #500

img = cv2.imread(path+"26.jpg")
cv2.namedWindow("About")
cv2.moveWindow("About",150,0)
cv2.imshow('About', cv2.resize(img,(1200,750)))
cv2.waitKey(0)
cv2.destroyAllWindows()
os.system("python home.py")