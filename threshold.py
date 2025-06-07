import cv2 as cv

img = cv.imread('./Photo/images.jpg')
cv.imshow('cat' , img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image' , gray) 
#There are three types of thresholding in OpenCV:
#1. Simple Thresholding 
#2. Adaptive Thresholding
#3. Otsu's Thresholding




#Simple Thresholding:
threshold , thresh = cv.threshold(gray, 150 ,255 , cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)


#Simple Thresholding (inverse):
threshold , thresh_inv = cv.threshold(gray, 150 ,255 , cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded inverse', thresh_inv)

#Adaptive Thresholding:
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholded ' , adaptive_thresh)

#Adaptive Thresholding (Gaussian):
adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholded Gaussian' , adaptive_thresh_gaussian)

cv.waitKey(0)