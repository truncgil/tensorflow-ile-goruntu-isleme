# Kütüphanelerimizi yükleyelim
import cv2 as cv
import imageio
# imageio kütüphanesini videoyu okumak ve video yazdırmak için kullanacağız
# Eğer imageio ve imageio-ffmpeg kütüphanesini yüklemediyseniz aşağıdaki terminal kodları ile yükleyebilirsiniz:
# pip install imageio
# pip install imageio-mpeg


# cv.CascadeClassifier fonksiyonu ile ön yüz cascade'imizi yüklüyoruz.
face_cascade = cv.CascadeClassifier('haarcascade-frontalface-default.xml')

# detect isminde bir fonksiyon oluşturalım. Burada frame adında bir parametre belirliyoruz. Bu fonksiyonu az sonra çağıracağız
def detect(frame):
    # Resmi gri renk şemasına dönüştürelim
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detectMultiScale() fonksiyonu ile verilen görüntüde CascadeClassifier fonksiyonu ile aldığımız cascade filtresini uyguluyoruz
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # Buradaki 1.1 değeri, resmin ne kadar küçültüleceğinin oranıdır
    # 5 değeri ise objenin minimum komşu sayısıdır


    # Birden fazla yüz olabilir. Bundan dolayı tamamını bir döngü içerisine yazacağız
    for (x, y, w, h) in faces:
        # Tespit edilen resimdeki yüzleri daha öncesinde gördüğümüz rectangle fonksiyonu ile kırmızı dikdörtgenler içerisine alıyoruz.
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)

        # Burada gri renk şeması üzerinde yüzün koordinatlarını belirliyoruz
        # y+h -> dikdörtgenin alt konumunu belirler
        # x+w -> dikdörtgenin sağ konumunu belirler
        gray_face = gray[y:y + h, x:x + w]

        # Burada da renkli resim üzerindeki yüzün koordinatlarını belirliyoruz
        color_face = frame[y:y + h, x:x + w]
        # Bu değerleri farklı şekillerde de kullanabilirsiniz

    # Sonrasında frame'i döndürüp fonksiyonu tamamlayalım
    return frame

# imageio kütüphanesini kullanarak girdi videomuzu okuyoruz
reader = imageio.get_reader('video.mp4')

# Burada fps ifadesini görüyoruz.
# Videolar saniyede peşpeşe 25-35 arası resimden oluşur. fps ifadesi de bunu ifade etmektedir.
fps = reader.get_meta_data()['fps']

# Burada da imageio kütüphanesinin writer fonksiyonunu kullanarak fps ile aldığımız resimleri videoya yazdırıyoruz
writer = imageio.get_writer('output.mp4', fps=fps)

# Aşağıdaki satır ile her bir fps için detect fonksiyonunu çalıştıracağız
for i, frame in enumerate(reader):
    # Yukarıda yazdığımız detect fonksiyonunu uyguluyoruz
    frame = detect(frame)

    # Buradaki append_data fonksiyonu ile her bir frame'i output videosuna ekliyoruz
    writer.append_data(frame)

    #Bir de kaçıncı frame'in işlendiğine bakalım
    print(i)

# Son olarak yazdığımız videoyu kapatalım
writer.close()