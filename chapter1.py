'''
Author: WHURS-THC
Date: 2022-10-21 20:37:07
LastEditTime: 2022-10-25 10:43:52
Description: 
'''
####################### READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# a=cv2.waitKey()
# print(type(a))

# ######################## READ VIDEO #############################
import cv2
frameWidth = 640
frameHeight = 4806
cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):# & ^ 与 或 异或运算 0xFF=1111 1111 取<255的部分,
        break
# ######################### READ WEBCAM  ############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10,150)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# ord('q')