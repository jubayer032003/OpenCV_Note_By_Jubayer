import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('./Photo/images.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRay' , gray)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)

masked = cv.bitwise_and(gray,gray,mask= mask)
cv.imshow('Masked', masked)

#Gray Scale Histogram
gray_hist = cv.calcHist([gray] , [0] , masked, [256] , [0,256])
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#color Histogram
plt.figure()
plt.title('Color Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors) :
    hist = cv.calcHist([img] ,[i] , masked , [256] ,[0,256])
    plt.plot(hist , color=col)
    plt.xlim([0,256]) 
plt.show()

cv.waitKey(0)