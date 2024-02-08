import cv2 #Image
import time # Delay
import imutils # Resize


cam = cv2.VideoCapture(0) ## initialize the camera
time.sleep(1)

firstFrame=None
area = 500

while True:
    _, img = cam.read() ## reading the frame from the camera
    text="Normal"
    img = imutils.resize(img, width=500) # resize

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Color 2 gray image

    gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0) ## Smoothened

    if firstFrame is None:
        firstFrame = gaussianImg ## Capturing 1st imag eon 1st iteration
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg) # absolute diff b/w 1st and current frame

    thresImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1] #Binary

    cnts = cv2.findContours(thresImg.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0),2)
        text = "Moving Object Detected"

    print(text)
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
               
    
