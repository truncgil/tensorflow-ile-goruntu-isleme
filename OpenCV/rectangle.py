import numpy as np
import cv2 as cv

src = cv.imread('image.jpg', cv.IMREAD_COLOR)

baslangic_noktasi = (15,15)
bitis_noktasi = (350,250)

#Renkler BGR olarak yani (Blue, Green, Red)(Mavi, Yeşil, Kırmızı) formatında yazılmalıdır
renk = (0,0,255)

kalinlik = 2

dst = cv.rectangle(src, baslangic_noktasi, bitis_noktasi, renk, kalinlik)

cv.imshow('src', src)
cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()