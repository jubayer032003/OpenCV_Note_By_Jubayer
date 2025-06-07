import cv2 as cv
import numpy as np

blank = np.zeros((400,400) , dtype = 'uint8')
# Create a rectangle
rectangle = cv.rectangle(blank.copy() , (30,30), (370,370) , 255, -1 )
cv.imshow('Rectangle' , rectangle)
#create a circle :
circle = cv.circle(blank.copy() ,(200,200), 200 , 255 , -1 )
cv.imshow('Circle' , circle)

# Bitwise AND --> (intersecting area of both shapes.This will show the area where both shapes overlap)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND' , bitwise_and)

#Bitwise OR --> (combines both shape areas. This will show the area covered by either shape)
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR' ,bitwise_or)

#Bitwise XOR --> non-overlapping areas of both shapes. This will show the area covered by either shape but not both)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR' , bitwise_xor)

#Bitwise NOT --> (inverts the shape. This will show the area not covered by the shape)
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT' , bitwise_not)

cv.waitKey(0)