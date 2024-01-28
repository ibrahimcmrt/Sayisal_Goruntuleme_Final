import cv2
import numpy as np
import os

# Görüntüyü yükle
image_path = "/Users/ibrahimcomert/Desktop/dilated_labels.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Bağlantı Bileşen Etiketleme
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)

# Her bir bileşen için sınır piksellerini bul
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Her bir bileşen için özelliklerin bulunduğu diziyi al
# stats dizisi her bir bileşen için [toplam_piksel_sayısı, sol_üst_x, sol_üst_y, genişlik, yükseklik] içerir
for label in range(1, num_labels):
    area = stats[label, cv2.CC_STAT_AREA]  # Bölge alanı
    perimeter = cv2.arcLength(contours[label - 1], True)  # Bölge çevresi

    # Alanın çevreye oranını hesapla
    area_perimeter_ratio = area / perimeter

    # Kompaktlığı hesapla
    compactness = (4 * np.pi * area) / (perimeter ** 2)

    # Sonuçları yazdır
    print(f"Bölge {label}:")
    print(f" - Alanın Çevreye Oranı: {area_perimeter_ratio}")
    print(f" - Kompaktlık: {compactness}")

# Daha fazla işlem yapmak için contour'ları görselde göster
# Bunun için orijinal görüntüyü renkli hale getiriyoruz
image_colored = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Her bir bileşeni çevreleyen konturları görselleştir
cv2.drawContours(image_colored, contours, -1, (0, 255, 0), 1)

# Sonuçları göster
cv2.imshow("Labeled Components with Contours", image_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()
