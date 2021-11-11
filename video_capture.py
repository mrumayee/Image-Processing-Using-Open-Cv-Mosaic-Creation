import cv2
import numpy as np
import random
# access the webcam
cap=cv2.VideoCapture(0)
while True:
    ret,shot=cap.read() 
    cv2.imshow("frame",shot)
    count=0
    k=cv2.waitKey(1)
    if  k==ord(" ")  : #space bar to get a screenshot
        my_image=shot.copy()
        cv2.imshow("Captured Image",shot)

    elif k== ord("q"):
        print("close")
        cv2.destroyAllWindows #q to close all the windows
        break
    elif k==ord("s"):
        cv2.imwrite("Capture"+str(count)+".jpg",shot)# s to save the image if necessary
        print("Image"+str(count)+"saved")
        count=+1





cap.release()




