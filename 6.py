import cv2
import numpy as np
import os

# Görüntüyü yükle
image_path = "/Users/ibrahimcomert/Desktop/dilated_labels.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Bağlantı Bileşen Etiketleme
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)

# Her bir bileşen için özelliklerin bulunduğu diziyi al
# stats dizisi her bir bileşen için [toplam_piksel_sayısı, sol_üst_x, sol_üst_y, genişlik, yükseklik] içerir
for label in range(1, num_labels):
    area = stats[label, cv2.CC_STAT_AREA]  # Bölge alanı
    left_top_x = stats[label, cv2.CC_STAT_LEFT]  # Sol üst köşenin x koordinatı
    left_top_y = stats[label, cv2.CC_STAT_TOP]  # Sol üst köşenin y koordinatı
    width = stats[label, cv2.CC_STAT_WIDTH]  # Bölge genişliği
    height = stats[label, cv2.CC_STAT_HEIGHT]  # Bölge yüksekliği

    # Bölgenin momentleri
    moments = cv2.moments((labels == label).astype(np.uint8))

    # Yön
    orientation = 0.5 * np.arctan2(2 * moments['mu11'], moments['mu20'] - moments['mu02'])

    # Dairesellik
    circularity = (4 * np.pi * area) / (width ** 2)

    # Sonuç
    print(f"Bölge {label}:")
    print(f" - Alan: {area}")
    print(f" - Yön: {orientation}")
    print(f" - Dairesellik: {circularity}")

    # Her bir bileşeni çevreleyen dikdörtgeni çiz
    cv2.rectangle(image, (left_top_x, left_top_y), (left_top_x + width, left_top_y + height), (255, 255, 255), 2)

# Sonuçları göster
cv2.imshow("Labeled Components", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
