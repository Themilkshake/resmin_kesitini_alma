import cv2
from cv2 import imshow
import numpy as np


araba = cv2.imread("rb.jpg")

#araba resminin kesitini alıp yeni değere atıyorum.
kesit = araba[100:200,200:500]

#resimden aldığımız kesiti resmin başka bir kısmına ekliyorum.
araba[0:100,0:300]=kesit
cv2.imshow("yeni araba", araba)


cv2.waitKey(0)
cv2.destroyAllWindows()