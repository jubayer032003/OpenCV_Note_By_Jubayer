import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('./haar_face.xml')
people = ['jeky_photo', 'jubayer_photo', 'priyo_photo']

# features = np.load('./features.npy')
# labels = np.load('./labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('./faces/priyo_photo/test04.jpg')
gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person' , img )

#detect the face :
face_rect = haar_cascade.detectMultiScale(gray, 1.1 , 4)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h , x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'label = {people[label]} with a confident of {confidence}')
    
    cv.putText(img, f'{people[label]} - {round(confidence, 2)}' , (20, 20) , cv.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 2)
    cv.rectangle(img, (x,y) , (x+w , y+h) , (0,255,0) , thickness=2)
cv.imshow('Detected face' , img)
cv.waitKey(0)