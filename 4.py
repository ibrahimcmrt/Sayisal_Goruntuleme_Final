import cv2
import numpy as np
import os

# Görüntüyü yükle
image_path = "/Users/ibrahimcomert/Desktop/edges_image.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Bağlantı Bileşen Etiketleme
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)

#print(stats)
#bölge dairesel yön
#labels.selected

# Dilasyon için kernel oluştur
kernel = np.ones((10, 10), np.uint8)

# Bağlantı bileşenlerini dilate et
dilated_labels = cv2.dilate(image, kernel, iterations=1)

# Sonuçları masaüstüne kaydet
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
cv2.imwrite(os.path.join(desktop_path, 'dilated_labels.png'), dilated_labels)

# Görselleri gösterme
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Labels", dilated_labels)
cv2.waitKey(0)
cv2.destroyAllWindows()
