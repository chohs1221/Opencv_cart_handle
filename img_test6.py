import numpy as np
import cv2
from img_test1 import *
from img_test2 import *
import time

start = time.time()

src = cv2.imread("12.jpg")
src = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
height, width, channel = src.shape
img_blur = Bluring(src, 15)
cv2.imshow('img_blur', img_blur)
img_binary = Grayscale(img_blur, 170)
cv2.imshow('img_binary', img_binary)
contours, img_contour = draw_Contours(img_binary, height, width, channel)
cv2.imshow('contours', img_contour)
lines = cv2.HoughLines(img_contour, 0.8, np.pi / 180, 150, srn = 100, stn = 200, min_theta = -20 * np.pi / 180, max_theta = 20 * np.pi / 180)

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
end = time.time()
print(end - start)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()