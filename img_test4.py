import numpy as np
import cv2
from img_test1 import *
from img_test2 import *
import time

start = time.time()

src = cv2.imread("11.jpg")
cv2.imshow("src",src)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
cv2.imshow("gray",binary)

kernel_erode = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
kernel_dilate = cv2.getStructuringElement(cv2.MORPH_CROSS, (6, 6))

erode = cv2.erode(binary, kernel_erode, anchor=(-1, -1), iterations=5)
cv2.imshow("erode",erode)

dilate = cv2.dilate(erode, kernel_dilate, anchor=(-1, -1), iterations=5)
cv2.imshow("dilate",dilate)

canny = cv2.Canny(dilate, 5000, 1500, apertureSize = 5, L2gradient = True)
cv2.imshow("canny",canny)

lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 90, srn = 10, stn = 200, min_theta = -20 * np.pi / 180, max_theta = 20 * np.pi / 180)

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

cv2.line(src, (x_min[1], y_min[1]), (x_min[2], y_min[2]), (0, 0, 255), 2)
cv2.line(src, (x_max[1], y_max[1]), (x_max[2], y_max[2]), (0, 0, 255), 2)
cv2.circle(src, (x_min[0], y_min[0]), 3, (255, 0, 0), 5, cv2.FILLED)
cv2.circle(src, (x_max[0], y_max[0]), 3, (255, 0, 0), 5, cv2.FILLED)
print(rho_min, rho_max)
print(np.arctan2(x_min[2]-x_min[1], y_min[2]-y_min[1]), np.arctan2(x_max[2]-x_max[1], y_max[2]-y_max[1]))
end = time.time()
print(end - start)

cv2.imshow("result", src)
cv2.waitKey(0)
cv2.destroyAllWindows()