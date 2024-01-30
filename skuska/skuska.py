# detekcia kruznic na hladanie hlav v obrazku
# pohlad zhora
# ludia v prilbach

import cv2 as cv
import numpy as np

obrazky = ['obr1.jpg', 'obr2.jpg', 'obr3.jpg', 'obr4.jpg', 'obr5.jpeg', 'obr6.jpg']

for nazov_obrazku in obrazky:

    cesta_k_obrazku = f'input/{nazov_obrazku}'

    img = cv.imread(cesta_k_obrazku)
    img2 = cv.imread(cesta_k_obrazku)

    scale_percent = 60
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim)

    resized_img = cv.resize(img, (696, 392))
    img = resized_img

    denoised_img = cv.medianBlur(img, 5)
    blur = cv.GaussianBlur(img,(5,5),0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    #gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    #denoised_img = cv.medianBlur(gray, 3)
    #denoised_img2 = cv.medianBlur(gray2, 3)

    edges = cv.Canny(gray, 100, 100)
    edges2 = cv.Canny(gray2, 100, 100)
    # tieto parametre su dobre na mnichoch - obr2
    #circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=25, minRadius=15, maxRadius=40)
    circles1 = cv.HoughCircles(edges2, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=23, minRadius=15, maxRadius=40)
    # obr3
    #circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=20, minRadius=12, maxRadius=50)
    # obr1
    #circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=20, minRadius=5, maxRadius=20)
    # obr4 - hokejisti
    #circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=17, minRadius=5, maxRadius=20)
    # obr5 - hokejisti
    #circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=16, minRadius=7, maxRadius=18)
    # obr6
    # circles1 = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=10, param2=17, minRadius=7, maxRadius=20)

    if circles1 is not None:
        circles1 = np.uint16(np.around(circles1))
        for i in circles1[0, :]:
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cesta_k_output = f'output/out_{nazov_obrazku}'
    cv.imwrite(cesta_k_output, img)




    # edges2 = cv.Canny(img2, 50, 50)
    # circles2 = cv.HoughCircles(edges2, cv.HOUGH_GRADIENT, 1, 20, param1=10, minRadius=5, maxRadius=60)
    # #circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=2, minDist=75, param1=170, param2=170, minRadius=10, maxRadius=400)
    # circles2 = circles2.tolist()
    # for cir in circles2:
    #    for x, y, r in cir:
    #        x, y, r = int(x), int(y), int(r)
    #        cv.circle(img2, (x, y), r, (0, 255, 0), 4)
    # cesta_k_output = f'output/out2_{nazov_obrazku}'
    # cv.imwrite(cesta_k_output, img2)



    # edges3 = cv.Canny(gray, 100, 100)
    # circles3 = cv.HoughCircles(edges3,cv.HOUGH_GRADIENT,1,20,
    #                         param1=50,param2=30,minRadius=0,maxRadius=50)
    #
    # circles = np.uint16(np.around(circles3))
    # for i in circles3[0,:]:
    # # draw the outer circle
    #     cv.circle(denoised_img2,(i[0],i[1]),i[2],(0,255,0),2)
    # # draw the center of the circle
    #     cv.circle(denoised_img2,(i[0],i[1]),2,(0,0,255),3)
    #
    # cesta_k_output3 = f'output/out3_{nazov_obrazku}'
    # cv.imwrite(cesta_k_output, denoised_img2)





