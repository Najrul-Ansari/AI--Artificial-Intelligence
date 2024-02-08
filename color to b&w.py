import cv2

img = cv2.imread("sample1.png") ## read an image

greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ## Color to grey

thresImg = cv2.threshold(greyImg,190,255,cv2.THRESH_BINARY)[1]

cv2.imwrite("thresholdImage3.jpg",thresImg)
