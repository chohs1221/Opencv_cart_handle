import img_test2
from img_test2 import cv2, np

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    h_ = img_test2.h_filter(h, 7, 30)
    s_ = img_test2.s_filter(s, 45, 70)
    v_ = img_test2.v_filter(v, 175, 240)

    hsv = cv2.merge([h_, s_, v_])
    cv2.imshow("result", hsv)


capture.release()
cv2.destroyAllWindows()