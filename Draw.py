import cv2 as cv
import numpy as np

#make a blank img : 
black = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Black', black)

#paint in  the img: (drawing rectangle and circle)
cv.rectangle(black ,(200,300) ,(300,400) , (0,255,0), thickness=cv.FILLED)
cv.circle(black, (250, 250),40, (255, 0, 0), thickness= cv.FILLED)
cv.line(black, (100 ,100), (500, 500), (255, 255, 255), thickness=1)
cv.imshow('Green', black)


#write text on the img:
cv.putText(black, 'Jubayer', (200, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', black)

# img = cv.imread('./Photo/images.jpg')
# cv.imshow('cat' , img)

cv.waitKey(0)