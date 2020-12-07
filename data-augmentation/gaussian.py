import cv2 as cv

img = cv.imread('images/10.jpg')

#Gaussian Blur
dst = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

cv.imshow('Orjinal Resim', img)
cv.imshow('Gaussian Blur', dst)
cv.waitKey(0)
cv.destroyAllWindows()