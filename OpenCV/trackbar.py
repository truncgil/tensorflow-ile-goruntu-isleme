import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Numpy ile siyah bir resim oluşturalım
img = np.zeros((300,512,3), np.uint8)

#'image' isminde bir pencere oluşturalım
cv.namedWindow('image')

# Red, Green, Blue için bir trackbar oluşturalım
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

# Renklerin ayarlanmasını sağlayan bir On/Off tuşu belirleyelim
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)

# Kontrol ettirirken sürekli olarak sonsuz döngü kullanmamız gerekiyor
while(1):
    cv.imshow('image',img)

    #Esc tuşuna basıldığında çıkacak
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # 4 adet trackbar'ın pozisyonlarını alıp bir değişkene atayalım
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

# Çıkışta belleği temizleyelim
cv.destroyAllWindows()