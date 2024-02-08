import cv2 ## importing cv2 library
import imutils ## Importing imutils library

img = cv2.imread("sample1.png") ## reading the image

resizeImg = imutils.resize(img,width=100) ## Resize an image

cv2.imwrite("resizedImg.jpg",resizeImg) ## save the resized image
