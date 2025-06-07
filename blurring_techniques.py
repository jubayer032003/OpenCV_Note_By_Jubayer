import cv2 as cv

img = cv.imread('./Photo/images.jpg')
cv.imshow('Image', img)

#Averaging
averaged = cv.blur(img , (7,7))
cv.imshow('Averaged' , averaged)

#Gaussian Blurring

gaussian_blurred = cv.GaussianBlur(img ,(7,7), 0)
cv.imshow('gaussian_blurred', gaussian_blurred)

#Median Blurring
mediam_blurred =cv.medianBlur(img, 7)
cv.imshow('Median Blurred' , mediam_blurred)

#Bilateral Bluring (recommended for edge preservation)
bilateral_blurred = cv.bilateralFilter(img,10 , 15 ,15)
cv.imshow('Bilateral Blurred' , bilateral_blurred)

cv.waitKey(0)