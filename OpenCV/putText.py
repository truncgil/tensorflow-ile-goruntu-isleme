import numpy as np
import cv2 as cv
import os, sys

src = cv.imread('image.jpg', cv.IMREAD_COLOR)

sol_alt = (80, 80)
font = cv.FONT_HERSHEY_SIMPLEX 
font_scale = 1
color = (255,0,255)
thickness = 2
text = "Merhaba Tensorflow"

dst = cv.putText(src, text, sol_alt, font, font_scale, color, thickness)

cv.imshow('image', src)
cv.imshow('src', dst)
cv.waitKey()
cv.destroyAllWindows()