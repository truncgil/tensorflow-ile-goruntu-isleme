import numpy as np
import cv2 as cv

src = cv.imread('image.jpg', cv.IMREAD_COLOR)

baslangic_noktasi = (155, 150)
bitis_noktasi = (350, 470)
renk = (255,0,0)
kalinlik = 5

dst = cv.line(src, baslangic_noktasi, bitis_noktasi, renk, kalinlik)

cv.imshow('src', src)
cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()