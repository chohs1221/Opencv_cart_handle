import numpy as np
import cv2
from img_test1 import *
from img_test2 import *
import time

def onChange(pos):
    pass

cv2.namedWindow("canny")

cv2.createTrackbar("canny_low", "canny", 0, 255, onChange)
cv2.setTrackbarPos("canny_low", "canny", 0)
cv2.createTrackbar("canny_high", "canny", 0, 255, onChange)
cv2.setTrackbarPos("canny_high", "canny", 255)
cv2.createTrackbar("line_threshold", "canny", 0, 255, onChange)
cv2.setTrackbarPos("line_threshold", "canny", 127)

while cv2.waitKey(33) != ord('q'):
    src = cv2.imread("11.jpg")
    src = cv2.resize(src, dsize=(1080, 720), interpolation=cv2.INTER_AREA)
    dst = src.copy()

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    canny_low = cv2.getTrackbarPos("canny_low", "canny")
    canny_high = cv2.getTrackbarPos("canny_high", "canny")
    canny = cv2.Canny(gray, canny_low, canny_high, apertureSize = 5, L2gradient = False)

    line_threshold = cv2.getTrackbarPos("line_threshold", "canny")
    lines = cv2.HoughLines(canny, 0.8, np.pi / 180, line_threshold, srn = 100, stn = 200, min_theta = -20 * np.pi / 180, max_theta = 20 * np.pi / 180)

    rho_min = 1e9
    rho_max = 0
    x_min = [0, 0, 0]
    y_min = [0, 0, 0]
    x_max = [0, 0, 0]
    y_max = [0, 0, 0]
    for i in lines:
        rho, theta = i[0][0], i[0][1]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a*rho, b*rho

        scale = src.shape[0] + src.shape[1]

        x1 = int(x0 + scale * -b)
        y1 = int(y0 + scale * a)
        x2 = int(x0 - scale * -b)
        y2 = int(y0 - scale * a)
        
        if rho < rho_min:
            rho_min = rho
            x_min[0], x_min[1], x_min[2] = x0, x1, x2
            y_min[0], y_min[1], y_min[2] = y0, y1, y2
        if rho > rho_max:
            rho_max = rho
            x_max[0], x_max[1], x_max[2] = x0, x1, x2
            y_max[0], y_max[1], y_max[2] = y0, y1, y2

    cv2.line(dst, (x_min[1], y_min[1]), (x_min[2], y_min[2]), (0, 0, 255), 2)
    cv2.line(dst, (x_max[1], y_max[1]), (x_max[2], y_max[2]), (0, 0, 255), 2)
    cv2.circle(dst, (x_min[0], y_min[0]), 3, (255, 0, 0), 5, cv2.FILLED)
    cv2.circle(dst, (x_max[0], y_max[0]), 3, (255, 0, 0), 5, cv2.FILLED)
    print(rho_min, rho_max)

    cv2.imshow("canny", dst)
    time.sleep(3000)