import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('./Photo/images.jpg')
cv.imshow('cat', img)
# plt.imshow(img)
# plt.show()

#BGR to gray scale :
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' ,gray)

#BGR to HSv :
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('hsv' , hsv ) 

#BGR to LAB :
lab = cv.cvtColor(img , cv.COLOR_BGR2Lab)
cv.imshow('Lab' , lab) 

#BGR to RGB :
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)  
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()

#HSV to BGR :
hsv_bgr = cv.cvtColor(hsv , cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR' , hsv_bgr)

#LAB to BGR :
lab_bgr = cv.cvtColor(lab , cv.COLOR_Lab2BGR)
cv.imshow('Lab to BGR ' , lab_bgr)


cv.waitKey(0)
cv.destroyAllWindows()