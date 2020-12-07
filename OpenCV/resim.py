import numpy as np
import cv2 as cv

src = cv.imread('image.jpg', cv.IMREAD_COLOR)
img = cv.imread('image.jpg', 0)

cv.imwrite('gray_image.jpg', img)

cv.imshow('image', img)
cv.imshow('src', src)
cv.waitKey()
cv.destroyAllWindows()