import cv2 as cv
# Read an image using OpenCV

img = cv.imread('./Photo/images.jpg')


cv.imshow('Image' , img)

#Read a video using OpenCV:

capture =cv.VideoCapture('./Video/do_video.mp4')
while True:
    isTrue,frame =capture.read()
    cv.imshow('Video' , frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()


cv.waitKey(0)
