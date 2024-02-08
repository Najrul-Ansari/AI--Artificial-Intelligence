import cv2
img = cv2.imread("sample1.png")

gaussianBlurImg = cv2.GaussianBlur(img,(25,25),0)

cv2.imwrite("gaussianImage.jpg", gaussianBlurImg)
