import img_test1
from img_test1 import cv2, np

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape

    img_blur = img_test1.Bluring(frame, 15)
    cv2.imshow('img_blur', img_blur)
    img_binary = img_test1.Grayscale(img_blur, 170)
    cv2.imshow('img_binary', img_binary)
    contours, img_contour = img_test1.draw_Contours(img_binary, height, width, channel)
    cv2.imshow('contours', img_contour)
    img_contourBox = img_test1.draw_ContourBox(img_contour, contours, 250, 3, height, width, channel)
    cv2.imshow('img_contourBox', img_contourBox)

    


capture.release()
cv2.destroyAllWindows()