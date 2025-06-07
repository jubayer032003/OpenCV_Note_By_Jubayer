# face detection ---> where the face is in the image
#face recognition ---> who the person is in the image
import cv2 as cv
img = cv.imread('./Photo/group_photo.jpg')
cv.imshow('Boy Image' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image' , gray)

haar_cascade = cv.CascadeClassifier('./haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1 , minNeighbors= 3)

print(f'Number of faces found = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y) ,(x+w ,y+h) ,(0,255,0) ,thickness=2 )
cv.imshow('Detected face' ,img ) 

cv.waitKey(0)