import cv2 as cv
import numpy as np
import imutils

image = cv.imread('images/q16.jpg')

# FLIPPING
# X ekseni etrafında
flipX = cv.flip(image, 0)
# Y ekseniz etrafında
flipY = cv.flip(image, 1)
# Her iki eksende de
flip2 = cv.flip(image, -1)
# BURADA TOPLAM 3 adet yeni resim elde etmiş olduk

# ROTATING
# Rotasyona uğratılan resimleri bir diziye ekleyelim
rotated = []
for angle in np.arange(90, 360, 90):
	rotated.append(imutils.rotate_bound(image, angle))
# BURADA DA TOPLAM 3 adet yeni resim elde etmiş olduk
# Daha anlaşılık bir şekilde yazarsak:
rotated_90 = rotated[0]
rotated_180 = rotated[1]
rotated_270 = rotated[2]
# TOPLAM 3 + 3 = 6 resim

# RESIZING
width = round(int(image.shape[1]) / 2)
height = round(int(image.shape[0]) / 2)
boyutlar = (width, height)

resized = cv.resize(image, boyutlar)
# BURADA TOPLAM 1 adet yeni resim elde etmiş olduk
# TOPLAM 6 + 1 = 7

gaussian = cv.GaussianBlur(image, (5,5), cv.BORDER_DEFAULT)
gaussian_90 = cv.GaussianBlur(rotated_90, (5,5), cv.BORDER_DEFAULT)
gaussian_180 = cv.GaussianBlur(rotated_180, (5,5), cv.BORDER_DEFAULT)
gaussian_270 = cv.GaussianBlur(rotated_270, (5,5), cv.BORDER_DEFAULT)
# Rotasyona uğratılmış resimlere Gaussian Blur metodunu uyguladık
# TOPLAM 7 + 4 = 11

gaussian_flipX = cv.GaussianBlur(flipX, (5,5), cv.BORDER_DEFAULT)
gaussian_flipY = cv.GaussianBlur(flipY, (5,5), cv.BORDER_DEFAULT)
gaussian_flip2 = cv.GaussianBlur(flip2, (5,5), cv.BORDER_DEFAULT)
# Çevrilmiş resimlere Gaussian Blur metodunu uyguladık
# TOPLAM 11 + 3 = 14

gaussian_resized = cv.GaussianBlur(resized, (5,5), cv.BORDER_DEFAULT)
# Boyutlandırılmış resme Gaussian Blur metodunu uyguladık
# TOPLAM 14 + 1 = 15

# Şimdi resimleri dst klasöründe dosyalara yazdıralım:
cv.imwrite('dst/original.jpg', image)
cv.imwrite('dst/flipX.jpg', flipX)
cv.imwrite('dst/flipY.jpg', flipY)
cv.imwrite('dst/flip2.jpg', flip2)
cv.imwrite('dst/rotated_90.jpg', rotated_90)
cv.imwrite('dst/rotated_180.jpg', rotated_180)
cv.imwrite('dst/rotated_270.jpg', rotated_270)
cv.imwrite('dst/resized.jpg', resized)
cv.imwrite('dst/gaussian.jpg', gaussian)
cv.imwrite('dst/gaussian_90.jpg', gaussian_90)
cv.imwrite('dst/gaussian_180.jpg', gaussian_180)
cv.imwrite('dst/gaussian_270.jpg', gaussian_270)
cv.imwrite('dst/gaussian_flipX.jpg', gaussian_flipX)
cv.imwrite('dst/gaussian_flipY.jpg', gaussian_flipY)
cv.imwrite('dst/gaussian_flip2.jpg', gaussian_flip2)
cv.imwrite('dst/gaussian_resized.jpg', gaussian_resized)

print('Bütün resimler kaydedildi')