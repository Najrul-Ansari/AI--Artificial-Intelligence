import cv2

img = cv2.imread("sample1.png") ## read an image

greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ## Color to grey

cv2.imwrite("greyimage.png", greyImg) ## Saving an image

cv2.imshow("Orig", img)
cv2.imshow("Gray", greyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
