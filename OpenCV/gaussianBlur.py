import numpy as np
import cv2 as cv

src = cv.imread('image.jpg', 0)
blured = cv.GaussianBlur(src, (15,15), 0)


cv.imshow('image', src)
cv.imshow('src', blured)
cv.waitKey()
cv.destroyAllWindows()