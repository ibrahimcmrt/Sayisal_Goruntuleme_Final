import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

# Görüntünün dosya yolunu belirtin
path = "/Users/ibrahimcomert/Desktop/keskinlestirilmis_resim.png"
img = cv.imread(path, 0)

img = cv.medianBlur(img, 5)

# Adaptive Gaussian Thresholding
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                            cv.THRESH_BINARY, 9, 13)

# Çerçeveyi kaldır
th3 = th3[5:-5, 5:-5]

# Çıktıyı masaüstüne kaydet
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
cv.imwrite(os.path.join(desktop_path, 'adaptive_thresholding_result.png'), th3)

# Resmi göster
plt.imshow(th3, 'gray')
plt.title('Adaptive Gaussian Thresholding')
plt.xticks([]), plt.yticks([])
plt.show()
