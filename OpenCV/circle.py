import numpy as np
import cv2 as cv

src = cv.imread('image.jpg', cv.IMREAD_COLOR)

merkez_koordinati = (155, 150)
yaricap = 50
renk = (0,0,255)
kalinlik = 2

dst = cv.circle(src, merkez_koordinati, yaricap, renk, kalinlik)

cv.imshow('src', src)
cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()