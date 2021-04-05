import img_test2
from img_test2 import cv2, np

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape

    dst = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 4000, 3500, apertureSize = 5, L2gradient = True)
    lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn = 100, stn = 200, min_theta = -20 * np.pi / 180, max_theta = 20 * np.pi / 180)

    rho_min = 1e9
    rho_max = 0
    x_min = [0, 0, 0]
    y_min = [0, 0, 0]
    x_max = [0, 0, 0]
    y_max = [0, 0, 0]
    
    try:
        if lines[0][0][0] == 1 and lines[0][0][1] == 1:
            continue
    except:
        pass
    for i in lines:
        rho, theta = i[0][0], i[0][1]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a*rho, b*rho

        scale = frame.shape[0] + frame.shape[1]

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
    cv2.imshow("dst", dst)


capture.release()
cv2.destroyAllWindows()