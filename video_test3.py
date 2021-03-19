from img_test1 import *
from img_test2 import *

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape

    low = [7, 20, 190]
    high = [30, 140, 250]
    img_masked = mask(frame, low, high)
    cv2.imshow("img_masked", img_masked)

    img_blur = Bluring(img_masked, 9)
    cv2.imshow('img_blur', img_blur)
    img_binary = Grayscale(img_blur, 100)
    cv2.imshow('img_binary', img_binary)
    contours, img_contour = draw_Contours(img_binary, height, width, channel)
    cv2.imshow('contours', img_contour)
    img_contourBox = draw_ContourBox(img_contour, contours, 300, 3, height, width, channel)
    cv2.imshow('img_contourBox', img_contourBox)


capture.release()
cv2.destroyAllWindows()