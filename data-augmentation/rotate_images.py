# Gerekli kütüphaneleri yükleyelim
import numpy as np
import imutils
import cv2

# Resmimizi okuyalım
image = cv2.imread('images/10.jpg')
 
# Döngümüzü oluşturalım
# Burada 0 ile 360 derece arasında 90'ar derece artacak şekilde bir döngü oluşturduk
# Yani resim 0, 90, 180, 270 derecelerde görünecek
for angle in np.arange(90, 360, 90):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated ", rotated)
	cv2.waitKey(0)