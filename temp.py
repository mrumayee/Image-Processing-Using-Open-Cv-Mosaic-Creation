import cv2
import numpy as np
import random as rd
import imutils

image = cv2.imread(r"E:\grand-mosque.jpg")
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, global_thresh = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY)


orig = np.copy(image)
width = global_thresh.shape[1]
height = global_thresh.shape[0]
rect = (0, 0, width, height)
subdiv = cv2.Subdiv2D(rect)

# points on the inside

# selects 100 random points on the image
for i in range(0, 100):
    randx = rd.randint(0, width)

    randy = rd.randint(0, height)
    subdiv.insert((randx, randy))

# edge points

# selects 10 random points on each side
for i in range(0, 10):
    subdiv.insert((0, rd.randint(0, height)))
    subdiv.insert((rd.randint(0, width), 0))
    subdiv.insert((width-1, rd.randint(0, height)))
    subdiv.insert((rd.randint(0, width), height-1))

# corners

subdiv.insert((0, 0))
subdiv.insert((0, height-1))
subdiv.insert((width-1, 0))
subdiv.insert((width-1, height-1))

triangleList = subdiv.getTriangleList()

for t in triangleList:
    pt1 = (t[0], t[1])
    pt2 = (t[2], t[3])
    pt3 = (t[4], t[5])

    # draws the triangles

    cv2.line(global_thresh, pt1, pt2, (0, 0, 0), 5)
    cv2.line(global_thresh, pt2, pt3, (0, 0, 0), 5)
    cv2.line(global_thresh, pt1, pt3, (0, 0, 0), 5)

contours, hierarchy = cv2.findContours(
    global_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# lower_blue=np.array([90,60,0])
# upper_blue=np.array([121,255,255])
# mask=cv2.inRange(hsv,lower_blue,upper_blue)
contours, hierarchy = cv2.findContours(
    global_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#contours=imutils.grab_contours(contours)
for contour in contours:
    #mask = np.zeros(global_thresh.shape, np.uint8)
    #cv2.drawContours(mask, c, -1, 255, -1)
    #mean = cv2.mean(global_thresh, mask=mask)
    #print(mean)
    approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(image,[approx],0,(0,0,0),2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    # M = cv2.moments(contour)
    # cX = int(M["m10"] / M["m00"])
    # cY = int(M["m01"] / M["m00"])
    # cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    # cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    if len(approx) == 3:
        cv2.putText(image, 'triangle', (x, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # compute the center of the contour

    # cnts = imutils.grab_contours()
    # c = max(cnts, key=cv2.contourArea)
    # extLeft = tuple(c[c[:, :, 0].argmin()][0])
    # extRight = tuple(c[c[:, :, 0].argmax()][0])
    # extTop = tuple(c[c[:, :, 1].argmin()][0])
    # extBot = tuple(c[c[:, :, 1].argmax()][0])
    area=cv2.contourArea(contour)
    if(area>100):
        M=cv2.moments(contour)
        cx=int(M["m10"] / M["m00"])
        cy=int(M["m01"] / M["m00"])
        #cv2.circle(image,(cx,cy),15,(255,0,0),-1)
        # print(image[cy][cx])
        b=int(image[cy][cx][0])
        g=int(image[cy][cx][1])
        r=int(image[cy][cx][2])
        # print(b)
        # print(g)
        # print(r)
        cv2.fillPoly(image,pts=[contour],color=(b,g,r))
cv2.namedWindow('orig', cv2.WINDOW_NORMAL)
cv2.imshow('orig', image)
cv2.imshow("Global_Thresh", global_thresh)
cv2.waitKey(0)
