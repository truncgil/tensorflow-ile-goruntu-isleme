import numpy as np
import cv2 as cv

#Resmi okuyalım
girdi = cv.imread('image.jpg', cv.IMREAD_COLOR)

#Resmin şeklini alalım
genislik, yukseklik, kanal = girdi.shape

#Dönderilecek resmin merkezini belirleyelim
merkez = (yukseklik // 2, genislik // 2)

#Transformasyon Matrisini belirleyelim
M = cv.getRotationMatrix2D(merkez, -45, 1.0)

#Ve döndürelim
cikti = cv.warpAffine(girdi, M, (genislik, yukseklik))

#Resmi ekranda gösterelim
cv.imshow('Girdi', girdi)
cv.imshow('Cikti', cikti)


cv.waitKey()
cv.destroyAllWindows()