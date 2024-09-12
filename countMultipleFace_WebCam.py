import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('Input/haarcascade_frontalface_default.xml')

# capture frames from a camera
cap = cv2.VideoCapture(0)
while 1:

	# reads frames from a camera
	ret, img = cap.read()

	# convert to gray scale of each frames
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		# To draw a rectangle in a face
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

	# Display an image in a window
	cv2.putText(img, "No of Faces = " + str(len(faces)), (100, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
	cv2.imshow('face Detection using Webcam',img)

	# Wait for Esc key to stop

	if cv2.waitKey(1) == 27:
		break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()