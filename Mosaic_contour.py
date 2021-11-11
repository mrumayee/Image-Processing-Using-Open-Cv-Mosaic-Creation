import cv2
import numpy as np
import random as rd

image = cv2.imread ("mos.jpg")
img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,global_thresh = cv2.threshold(img_gray,1,255,cv2.THRESH_BINARY)
orig = np.copy (image)
width = global_thresh.shape [1]
height = global_thresh.shape [0]
rect = (0, 0, width, height)
subdiv = cv2.Subdiv2D(rect)

# points on the inside

for i in range (0, 100):                                  # selects 100 random points on the image
    randx = rd.randint (0, width)

    randy = rd.randint (0, height)
    subdiv.insert ((randx, randy))

# edge points

for i in range (0, 10):                                   # selects 10 random points on each side
    subdiv.insert ((0, rd.randint(0, height)))
    subdiv.insert ((rd.randint(0, width), 0))
    subdiv.insert ((width-1, rd.randint(0, height)))
    subdiv.insert ((rd.randint(0, width), height-1))

# corners

subdiv.insert ((0, 0))
subdiv.insert ((0, height-1))
subdiv.insert ((width-1, 0))
subdiv.insert ((width-1, height-1))

triangleList = subdiv.getTriangleList ()

for t in triangleList:
    pt1 = (t[0], t[1])
    pt2 = (t[2], t[3])
    pt3 = (t[4], t[5])

    # draws the triangles

    cv2.line (global_thresh, pt1, pt2, (0, 0, 0), 5)
    cv2.line (global_thresh, pt2, pt3, (0, 0, 0), 5)
    cv2.line (global_thresh, pt1, pt3, (0, 0, 0), 5)

contours,hierarchy=cv2.findContours(global_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    #x=approx.ravel()[0]
    #y=approx.ravel()[1]
    #if len(approx)==3:
        #cv2.putText(image,'',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))


#cv2.namedWindow ('orig', cv2.WINDOW_NORMAL)
cv2.imshow ('orignal', image)
cv2.imshow("Global_Thresh",global_thresh)
cv2.waitKey (0)
