import cv2 as cv
import os
import numpy as np

people = ['jeky_photo', 'jubayer_photo', 'priyo_photo']
dir = r'C:\Users\ACW\Desktop\react\New folder\faces'

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

features =[]
labels = []

def create_tarin_data():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)
        for image in os.listdir(path):
            image_path = os.path.join(path, image)
            img_array =cv.imread(image_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in face_rect:
                face_roi = gray[y:y+h , x:x+w]
                features.append(face_roi)
                labels.append(label)
create_tarin_data()

print('Training Done ----------')

# print(f'Total features : {len(features)}')
# print(f'Total labels : {len(labels)}')
features = np.array(features, dtype = 'object')
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features , labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy' , features)
np.save('labels.npy' , labels )