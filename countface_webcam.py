# Import required modules
import cv2 as cv
import os
def getFaceBox(net, frame, conf_threshold=0.7):  # 1280 720
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]   # 480
    frameWidth = frameOpencvDnn.shape[1]    # 640
    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    # print("---------",detections)

    bboxes = []
    for i in range(detections.shape[2]):    # detections.shape[2] -> 200
        confidence = detections[0, 0, i, 2]
        # print(confidence)
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv.putText(frameOpencvDnn, "Face: " + str(len(bboxes)), (x1, y1-10), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (255, 255, 0), 2)
            # cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 0, 255), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, bboxes


faceProto = "Input/opencv_face_detector.pbtxt"
faceModel = "Input/opencv_face_detector_uint8.pb"
faceNet = cv.dnn.readNet(faceModel, faceProto)

cap = cv.VideoCapture(0)
while cv.waitKey(1) < 0:
    # Read frame
    hasFrame, frame = cap.read()
    # resized_frame = cv.resize(frame, (1100,720), interpolation=cv.INTER_AREA)

    if not hasFrame:
        cv.waitKey()
        break

    frameFace, bboxes = getFaceBox(faceNet, frame)
    # frameFace, bboxes = getFaceBox(faceNet, resized_frame)
    if not bboxes:
        print("No face Detected, Checking next frame")
        cv.putText(frameFace, "No face Found ", (10, 40), cv.FONT_HERSHEY_SIMPLEX*9, 1, (0, 0, 255), 2)
        cv.imshow("face Detection using Webcam", frameFace)
        continue

    for bbox in bboxes:
        if len(bboxes)==1:
            cv.putText(frameFace, "No of Face = " + str(len(bboxes)), (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 50), 2)
        else:
            cv.putText(frameFace, "No of Faces = " + str(len(bboxes)), (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 50), 2)
        cv.imshow("face Detection using Webcam", frameFace)

cap.release()
cv.destroyAllWindows()
cv.waitKey(100)
os.system("python home.py")