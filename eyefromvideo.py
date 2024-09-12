import cv2
#Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('Input/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Input/haarcascade_eye_tree_eyeglasses.xml')


#Variable store execution state
first_read = True

#Starting the video capture
cap = cv2.VideoCapture('Input/videos/eye_detection.mp4')
ret,img = cap.read()

while(ret):
    ret,img = cap.read()
    #Coverting the recorded image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Applying filter to remove impurities
    gray = cv2.bilateralFilter(gray,5,1,1)

    #Detecting the face for region of image to be fed to eye classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(len(faces)>0):
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            #roi_face is face which is input to eye classifier
            roi_face = gray[y:y+h,x:x+w]
            roi_face_clr = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_face,1.287,4)   # 1.293,4
            # print(eyes)
            #Examining the length of eyes object for eyes
            if(len(eyes)>=2):
                #Check if program is running for detection
                if(first_read):
                    cv2.putText(img, "Eyes Open", (50,70), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            else:
                if(first_read):
                    cv2.putText(img, "Eyes Closed", (50,70), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
                    cv2.waitKey(5)
    else:
        cv2.putText(img,"No face detected",(100,100),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)

    #Controlling the algorithm with keys
    cv2.imshow('img',img)
    a = cv2.waitKey(10)
    if(a==27):     # press escape key
        break

cap.release()
cv2.destroyAllWindows()