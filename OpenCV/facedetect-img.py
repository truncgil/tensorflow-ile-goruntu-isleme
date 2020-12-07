import cv2 as cv
import imageio

face_cascade = cv.CascadeClassifier('haarcascade-frontalface-default.xml')

# Fonksiyonumuzu belirleyelim
def detect(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
    return frame

# Resmimizi okutup yazdırabiliriz
image = imageio.imread('face.jpeg')
image = detect(frame=image)
imageio.imwrite('output.jpg', image)