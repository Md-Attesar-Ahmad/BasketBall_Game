import cv2
import numpy as np
import math

botx = 0.0
boty = 600.0
time = 0.0
xcon = 0.0
ycon = 0.0
vel = 0.0
st = 0
he = 0.0
x1 = 0
y1 = 0
k = 0
blank = np.ones((780, 1400, 3), np.uint8)
cv2.namedWindow("basket_ball")
cv2.circle(blank, (int(botx), int(780-boty)), 10, (0, 0, 255), -1)


def basketpos(event, x, y, flags, param):
    global st, xcon, ycon, blank, x1, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        st = 1
        xcon = x
        ycon = y
        x1 = int(x+(50.0/1.414))
        y1 = int(y+(50.0/1.414))
        x2 = int(x-(50.0/1.414))
        y2 = int(y-(50.0/1.414))
        blank = cv2.flip(blank, 0)
        cv2.rectangle(blank, (x1, y1), (x2, y2), (255, 0, 0), 4)


def path(x, y):
    global blank, x1, y1, k, xcon
    if(xcon-x < 30):
        k = 1
    blank = cv2.flip(blank, 0)
    cv2.circle(blank, (x, y), 20, (255, 255, 255), -1)


cv2.setMouseCallback("basket_ball", basketpos)
while True:
    if st == 1:
        vel = ((xcon)/math.cos(0.7854)) * \
            (math.sqrt(9.8/(2.0*(xcon*math.tan(0.7854)+780-boty-780+ycon))))
        x2 = (time)*vel*math.cos(0.7854)
        y2 = time*vel*math.sin(0.7854)-9.8*0.5*time*time+780-boty
        x2 = int(x2)
        y2 = int(y2)
        path(x2, y2)
        time = time+0.6
    blank = cv2.flip(blank, 0)
    cv2.imshow("basket_ball", blank)
    a = cv2.waitKey(100)
    if a == ord('q'):
        break
    if k == 1:
        break
cv2.imshow("basket_ball", blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
