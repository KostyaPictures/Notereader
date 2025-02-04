#       ТРЕБОВАНИЯ (скоро их станет меньше)
#512x100 исключительно
#идеальные фотки под идеальным кглом и идеальной перспективой
#идеально чёрные и белые цвета
#только простые ноты и без доп. строк

import cv2
import numpy as np

"""cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""



img = cv2.imread('notesinger/notes.png', cv2.IMREAD_GRAYSCALE) #Загружаем изображение в оттенках серого

y, x = img.shape #Получение размера изображения

img_inv = cv2.bitwise_not(img) #Инвертируем изображение, чтобы черные точки стали белыми (255), а фон черным (0)

i=0 #y
oi=0 #old index
stry=[] #Strings Y possitions
arrl=[] #Arrage of lenth (delta l)
for i in range(y): #Делаем проверку линий (mean() делает среднее арифметическое)
    i+=1
    m=int(np.mean(img_inv[i-1:i,0:x])) #mean
    if m>=127:
        stry.append(i-1)
        arrl.append(i-oi)
        oi=i
noteh=int(arrl[1]/2+1) #note height

ix=0 #index x
iy=0 #index y


for ix in range(x//noteh):
    for iy in range(y):
        m=np.mean(img_inv[iy:(iy+noteh),ix:(ix+noteh)])
        if m>=192:
            g=0
            ml=[] #minimal list
            for g in range(5):
                ml.append(stry[g]-(iy+noteh//2))
                g+=1
            mi=ml.index(min(ml)) #min index
            if mi==0:
                print("1-ая строка")
            if mi==1:
                print("2-ая строка")
            if mi==2:
                print("3-яя строка")
            if mi==3:
                print("4-ая строка")
            if mi==4:
                print("5-ая строка")
        iy+=noteh//2
    ix+=noteh//2



print(stry,arrl,noteh)




