'''
Author: WHURS-THC
Date: 2022-10-21 20:37:07
LastEditTime: 2022-10-24 21:51:06
Description: 
'''
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350
dst=np.zeros((height,width),dtype=np.uint8)
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width+10,height+200),borderMode=cv2.BORDER_CONSTANT)

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)