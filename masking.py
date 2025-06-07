import cv2 as cv
import numpy as np

img = cv.imread('./Photo/images.jpg')
cv.imshow('cat' , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('BLank' , blank)

mask = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Mask' , mask)

masked = cv.bitwise_and(img,img,mask= mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)