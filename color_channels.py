import cv2 as cv
import numpy as np

img = cv.imread('./Photo/images.jpg')
cv.imshow('Image' , img)
b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank , blank])
green = cv.merge([blank , g , blank])
red = cv.merge([blank, blank , r])
# Split the image into its color channels

cv.imshow('BLue' , blue)
cv.imshow('Green', green)
cv.imshow('Red', red)



print('original image shape:', img.shape)
print('Blue channel shape:', b.shape)
print('Green channel shape:', g.shape)
print('Red channel shape:', r.shape)



# Merge the channels back together
merged = cv.merge((b, g, r))
cv.imshow('Merged Image', merged)


cv.waitKey(0)
cv.destroyAllWindows()