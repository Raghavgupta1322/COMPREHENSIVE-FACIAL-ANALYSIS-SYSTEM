import cv2
import os
list = ['1.jpg','1p.jpg']
list1 = ['7p.jpg']
for i in list:
    img = cv2.imread(i)
cv2.imshow('Loading...', cv2.resize(img,(900,677)))
cv2.waitKey(1200)#1200
for i in list1:
    img = cv2.imread(i)
    cv2.imshow('Loading...', cv2.resize(img,(900,677)))   # cv2.resize(img,(900,677))
    cv2.waitKey(2000)
cv2.destroyAllWindows()
os.system("python interface.py")