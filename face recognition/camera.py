import cv2
import numpy as np
import face_recognition
cap = cv2.VideoCapture(0)# get frame frome camera


encode = input("Open encoding? Y/N  ")

if encode == 'Y':
    my_image = face_recognition.load_image_file("face source\me.jpg")
    my_face_encoding = face_recognition.face_encodings(my_image)[0]




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
    
    if encode == 'Y':
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []
    
    print (face_locations)

    faceNum = len(face_locations)

    if encode == 'Y':
        #在图像里找我自己
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([my_face_encoding], face_encoding)
            name = "Unknown"

            if match[0]:
                name = "Me"

            face_names.append(name)

        process_this_frame = not process_this_frame

    
    
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

        #矩形
        cv2.rectangle(frame, (left, top), (right, bottom), (55,255,155), 2)


        if encode == 'Y':
            #加上标签
            #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            #这个矩形丑到爆炸，删了。。
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    
    cv2.imshow('Video', frame)
    



       
    if cv2.waitKey(1) & 0xFF == ord('q'):      
        breakcap.release()
cv2.destroyAllWindows()
