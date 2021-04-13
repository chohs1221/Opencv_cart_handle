import img_test2
from img_test2 import cv2, np
import time

def onChange(pos):
    pass

cv2.namedWindow("result")

cv2.createTrackbar("tresh", "result", 0, 255, onChange)
cv2.createTrackbar("canny_L", "result", 0, 255, onChange)
cv2.createTrackbar("canny_H", "result", 0, 255, onChange)

cv2.setTrackbarPos("tresh", "result", 155)
cv2.setTrackbarPos("canny_L", "result", 155)
cv2.setTrackbarPos("canny_H", "result", 255)

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

tresh = 75
canny_L_H = [155, 255]
while cv2.waitKey(33) != ord('q'):
    tresh = cv2.getTrackbarPos("tresh", "result")
    canny_L_H[0] = cv2.getTrackbarPos("canny_L", "result")
    canny_L_H[1] = cv2.getTrackbarPos("canny_H", "result")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape
    dst = frame.copy()

    hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, tresh, 255, cv2.THRESH_BINARY)
    cv2.imshow("gray",binary)

    kernel_erode = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
    kernel_dilate = cv2.getStructuringElement(cv2.MORPH_CROSS, (6, 6))

    erode = cv2.erode(binary, kernel_erode, anchor=(-1, -1), iterations=5)
    cv2.imshow("erode",erode)

    dilate = cv2.dilate(erode, kernel_dilate, anchor=(-1, -1), iterations=5)
    cv2.imshow("dilate",dilate)

    canny = cv2.Canny(dilate, canny_L_H[0], canny_L_H[1], apertureSize = 5, L2gradient = True)
    cv2.imshow("canny",canny)

    lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 100, srn = 100, stn = 200, min_theta = -30 * np.pi / 180, max_theta = 30 * np.pi / 180)

    rho_min = 1e9
    rho_max = 0
    x_min = [0, 0, 0]
    y_min = [0, 0, 0]
    x_max = [0, 0, 0]
    y_max = [0, 0, 0]
    print(canny_L_H, tresh)
    try:
        for i in lines:
            rho, theta = i[0][0], i[0][1]
            a, b = np.cos(theta), np.sin(theta)
            x0, y0 = a*rho, b*rho

            scale = height + width

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
        print(np.arctan2(x_min[2]-x_min[1], y_min[2]-y_min[1]), np.arctan2(x_max[2]-x_max[1], y_max[2]-y_max[1]))
        cv2.imshow("result", dst)

    except TypeError:
        print("TypeError")
        continue
    except OverflowError:
        print("OverflowError")
        continue

    time.sleep(0.1)




capture.release()
cv2.destroyAllWindows()