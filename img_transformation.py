import cv2 as cv
import numpy as np 
img = cv.imread('./Photo/images.jpg')

def translate(img, x, y) :
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img, transMat ,  dimensions)

# -x --->  left
# -y --->  up
# +x --->  right    
# +y --->  down
translated = translate(img, -100, -100)
cv.imshow('translated' ,translated)


#rotation :

def rotate(img, angle , rotPoint = None ) :
    (heigth , width ) = img.shape[:2]
    if rotPoint is None :
        rotPoint = (width //2 , heigth //2)

    rotPoint = cv.getRotationMatrix2D(rotPoint ,angle ,1.0)
    diamensions = (width, heigth)
    return cv.warpAffine(img, rotPoint, diamensions)
rotated = rotate(img, 180)
cv.imshow('rotated', rotated)

# resizing :

resized = cv. resize(img , (200,200), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized' , resized)

# flipping :
# 0 ---> horizontal
# 1 ---> vertical
#-1 ---> both
flipped = cv. flip(img , 1)
cv.imshow('Filpped' ,flipped)

# Cropping :
cropped = img [200:400 , 100 :200]
cv.imshow('cropped' , cropped)

cv.waitKey(0)