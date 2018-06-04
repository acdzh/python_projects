import cv2
import numpy as np
import face_recognition
cap = cv2.VideoCapture("input.mp4")

#
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while(1):    # get a frame and show   
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    print (face_locations)

    faceNum = len(face_locations)
    for i in range(0, faceNum):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top =  face_locations[i][0]
        right =  face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 矩形框
        cv2.rectangle(frame, (left, top), (right, bottom), (55,255,155), 3)


    
    cv2.imshow('Video', frame)
    








       
    if cv2.waitKey(1) & 0xFF == ord('q'):      
        breakcap.release()
cv2.destroyAllWindows()
