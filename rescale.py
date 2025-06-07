import cv2 as cv

def rescale_frame(frame , scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimantions = (width,height)

    return cv.resize(frame,dimantions, interpolation= cv.INTER_AREA)

#resize an image using OpenCV:
img = cv.imread('./Photo/images.jpg')
cv.imshow('Image' , img)
img_resized = rescale_frame(img, scale = 0.2)
cv.imshow('Resized Image' , img_resized)

#Resize a video using OpenCV:

capture =cv.VideoCapture('./Video/do_video.mp4')
while True:
    isTrue,frame =capture.read()

    frame_resized = rescale_frame(frame, scale=0.2)
    cv.imshow('Resized Video', frame_resized)

    cv.imshow('Video' , frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()


cv.waitKey(0)

