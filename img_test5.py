import numpy as np
import cv2

src = cv2.imread("11.jpg")

lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 0, minLineLength = 10, maxLineGap = 100)

angle_min = 1e9
angle_max = 0
x = [[0, 0], [0, 0]]
y = [[0, 0], [0, 0]]
for i in lines:
    x1, y1 = i[0][0], i[0][1]
    x2, y2 = i[0][2], i[0][3]
    temp = np.arctan2(y1-y2, x2-x1)
    
    if temp < angle_min:
        angle_min = temp
        x[0][0], x[0][1], y[0][0], y[0][1] = x1, x2, y1, y2
    if temp > angle_max:
        angle_max = temp
        x[1][0], x[1][1], y[1][0], y[1][1] = x1, x2, y1, y2

cv2.line(dst, (x[0][0], y[0][0]), (x[0][1], y[0][1]), (0, 0, 255), 2)
cv2.line(dst, (x[1][0], y[1][0]), (x[1][1], y[1][1]), (0, 0, 255), 2)
print("x: {}\ny: {}".format(x, y))
print("angle_min: {}\nangle_max: {}".format(angle_min, angle_max))
for i in lines:
    cv2.line(dst, (i[0][0], i[0][0]), (i[0][1], i[0][1]), (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()