import cv2
import numpy as np

# Загружаем изображение в оттенках серого
img = cv2.imread('D:/prog/notesinger/notes.png', cv2.IMREAD_GRAYSCALE)
"""cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

# Инвертируем изображение, чтобы черные точки стали белыми, а фон черным
img_inv = cv2.bitwise_not(img)

print(img_inv[0:2,0:2])




