#import opencv
import cv2

#import the image
img = cv2. imread('97e005cf1fb5248919a9b3540682251.jpg')

#edit the image
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create a face detection classifier
faceCascade = cv2.CascadeClassifier('face_detect.xml')

#detect the number of faces
faceRect = faceCascade.detectMultiScale(gray, 1.1, 8)

#print the number of faces
print(len(faceRect))

#loop through the list of faces and extract each one
for i, (x, y, w, h) in enumerate(faceRect):
    #extract the face from the original image
    face = img[y:y + h, x:x + w]

    #save the extracted face as a separate image
    cv2.imwrite('face_{}.jpg'.format(i), face)

    #display the extracted face
    cv2.imshow('Face {}'.format(i), face)

    #surround the faces with a rectangle
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#show the image
cv2.imshow('img',img)

#wait until key is pressed
cv2.waitKey(0)