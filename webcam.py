import cv2 as cv
#Read a video using OpenCV:
# Open the default webcam (0)
capture = cv.VideoCapture(0)

# Check if the webcam is opened correctly
if not capture.isOpened():
    print("Error: Could not open video capture")
    exit()

while True:
    # Read one frame
    isTrue, frame = capture.read()

    if not isTrue:
        print("Failed to read frame")
        break

    # Show the frame
    cv.imshow('Webcam', frame)

    # Press 'q' to break the loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
capture.release()
