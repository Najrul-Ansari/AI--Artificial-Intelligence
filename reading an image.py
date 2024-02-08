import cv2

img = cv2.imread('sample1.png')  ##reading an image

cv2.imwrite('newlogo.png',img) ## Saving the read image

cv2.imshow("PS LOGO",img) ## Display the  image
cv2.waitKey(0)

cv2.destroyAllWindows()
