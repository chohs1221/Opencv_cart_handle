import cv2
import numpy as np

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape

    # 블러링
    img_blur = cv2.blur(frame, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
    # 그레이스케일
    gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)
    # 컨투어
    contours, _ = cv2.findContours(
        binary, 
        mode=cv2.RETR_LIST, 
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    cv2.drawContours(temp_result, contours=contours, contourIdx=-1, color=(255, 255, 255))
    cv2.imshow('contours', temp_result)
    # 컨투어 박스
    temp_result = np.zeros((height, width, channel), dtype=np.uint8)

    contours_dict = []

    for contour in contours:
        rect = cv2.minAreaRect(contour)
        if rect[1][0] > 250 and (rect[1][0] // rect[1][1]) > 5:
            box = cv2.boxPoints(rect)
            box = np.int0(box) 
            cv2.drawContours(temp_result, [box], -1, (0, 255, 0), 2)
    cv2.imshow('result', temp_result)


capture.release()
cv2.destroyAllWindows()