import cv2 as cv
import numpy as np
img = cv.imread('./Photo/images.jpg')
cv.imshow('cat' , img)

blank = np.zeros(img.shape , dtype='uint8')
cv.imshow('Blank Image' , blank)


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' ,gray)

# blur =cv.GaussianBlur(gray , (5,5) , cv.BORDER_DEFAULT)
# cv.imshow('Blurred Image', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges ' , canny)

ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded Image', thresh)

contours , hierarchy = cv.findContours( thresh , cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'Number of contours found: {len(contours)}')


cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)