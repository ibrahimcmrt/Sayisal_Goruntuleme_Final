import cv2
import numpy as np
import os

# Görüntüyü oku
image_path = "/Users/ibrahimcomert/Desktop/adaptive_thresholding_result.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Eşikleme işlemi
_, thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Bileşen boyutlarına göre filtreleme
min_component_size = 1000  # Filtreleme için minimum bileşen boyutu
filtered_image = np.zeros_like(thresholded)
_, labels, stats, _ = cv2.connectedComponentsWithStats(thresholded, connectivity=8)
for label in range(1, len(stats)):
    if stats[label, cv2.CC_STAT_AREA] >= min_component_size:
        filtered_image[labels == label] = 255

# Erozyon işlemi kernel
kernel = np.ones((2, 2), np.uint8)

# Erozyon işlemini uygula
eroded_image = cv2.erode(filtered_image, kernel, iterations=1)

# Filtrelenmiş ve erozyon uygulanmış görüntüyü kaydet
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
cv2.imwrite(os.path.join(desktop_path, 'filtered_and_eroded_image.jpg'), eroded_image)

# Kenarları bulma
edges = cv2.Canny(eroded_image, 100, 200)

# Kenarlıklı görüntüyü kaydet
cv2.imwrite(os.path.join(desktop_path, 'edges_image.jpg'), edges)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Filtered and Eroded Image', eroded_image)
#cv2.imshow('Edges Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Uyarı mesajı
print("Filtreleme, erozyon ve kenar bulma işlemi tamamlandı. Sonuçlar masaüstüne kaydedildi.")
