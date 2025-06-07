import cv2 as cv
import numpy as np 

img = cv.imread('./Photo/images.jpg')
cv.imshow('cat' , img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image' , gray)

# Laplacian Gradient
lap =cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

#Sobel Gradient :
sobel_x = cv.Sobel(gray , cv.CV_64F , 1 ,0)
sobel_y = cv.Sobel(gray , cv.CV_64F ,0,1)

combined_sobel = cv.bitwise_or(sobel_x,sobel_y)

canny = cv.Canny(gray,150,175)

cv.imshow('Sobel X' , sobel_x)
cv.imshow('Sobel Y' , sobel_y)
cv.imshow('Combined Sobel ' , combined_sobel)
cv.imshow("laplacian " , lap )
cv.imshow('Canny' , canny)





cv.waitKey(0)