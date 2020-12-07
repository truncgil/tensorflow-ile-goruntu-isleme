import cv2 as cv

image = cv.imread('images/10.jpg')

# X ekseni etrafında
flipX = cv.flip(image, 0)

# Y ekseniz etrafında
flipY = cv.flip(image, 1)

# Her iki eksende de
flip2 = cv.flip(image, -1)

# Resimlerimizi gösterelim
cv.imshow('Orjinal Resim', image)
cv.imshow('X ekseni etrafinda', flipX)
cv.imshow('Y ekseni etrafinda', flipY)
cv.imshow('Her iki eksende de', flip2)

# Bekleme fonksiyonumuzu çalıştıralım
cv.waitKey(0)

# Beklemeden çıkıldıktan sonra RAM'de kalan verileri temizleyelim
cv.destroyAllWindows()