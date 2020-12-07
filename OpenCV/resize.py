import numpy as np
import cv2 as cv

src = cv.imread('image.jpg', cv.IMREAD_COLOR)

# Resmin boyutlarını alalım
width = src.shape[1]
height = src.shape[0]

#Resmin genişliğini ve yüksekliğini yarı oranına düşürelim
dimension = (int(width/2), int(height/2))

#boyutlandırma işlemi
dst = cv.resize(src, dimension)

cv.imshow('src', src)
cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()