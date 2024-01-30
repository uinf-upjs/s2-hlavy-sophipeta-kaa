import cv2 as cv
import numpy as np

#obrazky = ['obr1.jpg', 'obr2.jpg', 'obr3.jpg', 'obr4.jpg', 'obr5.jpeg']

img1 = cv.imread('input/obr1.jpg') #720*429
denoised_img1 = cv.medianBlur(img1, 3)
gray1 = cv.cvtColor(denoised_img1, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray1, 100, 100)
circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=20, minRadius=5, maxRadius=20)
if circles1 is not None:
        circles1 = np.uint16(np.around(circles1))
        for i in circles1[0, :]:
            cv.circle(img1, (i[0], i[1]), i[2], (0, 255, 0), 2)
cv.imwrite('output/out4_obr1', img1)
