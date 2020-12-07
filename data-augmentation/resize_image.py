# OpenCV'yi dahil edelim
import cv2 as cv

# Resmi okuyalım
img = cv.imread('images/10.jpg')

# Resmin yarı boyutunu hesaplayalım
# img.shape[1], resmin genişliğini vermektedir
width = round(int(img.shape[1]) / 2)

# img.shape[0], resmin yüksekliğini vermektedir
height = round(int(img.shape[0]) / 2)

# boyut dizisi oluşturalım
boyutlar = (width, height)

resized = cv.resize(img, boyutlar)

cv.imshow('Orjinal Resim', img)
cv.imshow('Boyutlandirilmis Resim', resized)

cv.waitKey(0)
cv.destroyAllWindows()
