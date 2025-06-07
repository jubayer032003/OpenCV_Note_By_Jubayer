import cv2 as cv
img = cv.imread('./Photo/images.jpg')
cv.imshow('Image' , img)

#convarting to grayscale img:

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image' , gray)

#blurring the imagte:
blur =cv.GaussianBlur(img,(99,99),cv.BORDER_DEFAULT)
cv.imshow('Blured image' , blur)

#edges in the image : 
edges = cv.Canny(img,125,175)
cv.imshow('Canny Edges' , edges)

#dilating the image :
dilated = cv.dilate(edges ,(7,7) ,iterations= 2) 
cv.imshow('Dilated image' , dilated)

#eroding the image  : 
eroding =cv.erode(dilated,(7,7) , iterations= 2 )
cv.imshow('Eroded image ' , eroding)

#Resize the image :
resized = cv.resize(img,(200,200) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image' , resized)

#cropping : 
cropped = img[50:200, 200:400]
cv.imshow('Cropped image' , cropped)





cv.waitKey(0)