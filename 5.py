import cv2
import numpy as np
import os

# Görüntüyü yükle
image_path = "/Users/ibrahimcomert/Desktop/dilated_labels.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Bağlantı Bileşen Etiketleme
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)


# Rastgele renkler oluştur
colors = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)

# Arka planı siyah yap
colored_labels = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Bileşenleri farklı renklerle renklendir
for label in range(1, num_labels):
    colored_labels[labels == label] = colors[label]

# Sonuçları masaüstüne kaydet
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
cv2.imwrite(os.path.join(desktop_path, 'colored_labels.png'), colored_labels)

# Görselleri gösterme
cv2.imshow("Original Image", image)
cv2.imshow("Colored Labels", colored_labels)
cv2.waitKey(0)
cv2.destroyAllWindows()
