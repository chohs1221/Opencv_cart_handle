from img_test1 import *
from img_test2 import *

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def onChange(pos):
    pass

cv2.namedWindow("img_contourBox")

cv2.createTrackbar("h_min", "img_contourBox", 0, 179, onChange)
cv2.createTrackbar("h_max", "img_contourBox", 0, 179, onChange)
cv2.createTrackbar("s_min", "img_contourBox", 0, 255, onChange)
cv2.createTrackbar("s_max", "img_contourBox", 0, 255, onChange)
cv2.createTrackbar("v_min", "img_contourBox", 0, 255, onChange)
cv2.createTrackbar("v_max", "img_contourBox", 0, 255, onChange)
cv2.createTrackbar("blur", "img_contourBox", 5, 15, onChange)
cv2.createTrackbar("g_scale", "img_contourBox", 0, 255, onChange)

cv2.setTrackbarPos("h_min", "img_contourBox", 7)
cv2.setTrackbarPos("h_max", "img_contourBox", 30)
cv2.setTrackbarPos("s_min", "img_contourBox", 20)
cv2.setTrackbarPos("s_max", "img_contourBox", 140)
cv2.setTrackbarPos("v_min", "img_contourBox", 190)
cv2.setTrackbarPos("v_max", "img_contourBox", 250)
cv2.setTrackbarPos("blur", "img_contourBox", 9)
cv2.setTrackbarPos("g_scale", "img_contourBox", 100)

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    height, width, channel = frame.shape

    low = [7, 20, 190]
    high = [30, 140, 250]
    low[0] = cv2.getTrackbarPos("h_min", "img_contourBox")
    high[0] = cv2.getTrackbarPos("h_max", "img_contourBox")
    low[1] = cv2.getTrackbarPos("s_min", "img_contourBox")
    high[1] = cv2.getTrackbarPos("s_max", "img_contourBox")
    low[2] = cv2.getTrackbarPos("v_min", "img_contourBox")
    high[2] = cv2.getTrackbarPos("v_max", "img_contourBox")
    blur = cv2.getTrackbarPos("blur", "img_contourBox")
    g_scale = cv2.getTrackbarPos("g_scale", "img_contourBox")

    img_masked = mask(frame, low, high)
    cv2.imshow("img_masked", img_masked)

    img_blur = Bluring(img_masked, blur)
    cv2.imshow('img_blur', img_blur)

    img_binary = Grayscale(img_blur, g_scale)
    cv2.imshow('img_binary', img_binary)

    contours, img_contour = draw_Contours(img_binary, height, width, channel)
    cv2.imshow('contours', img_contour)

    img_contourBox = draw_ContourBox(img_contour, contours, 300, 3, height, width, channel, frame)
    cv2.putText(img_contourBox, "h: ("+str(low[0])+", "+str(high[0])+")", (10, 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(img_contourBox, "s: ("+str(low[1])+", "+str(high[1])+")", (10, 25), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(img_contourBox, "v: ("+str(low[2])+", "+str(high[2])+")", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
    cv2.imshow('img_contourBox', img_contourBox)

    if cv2.waitKey(33) == ord('r'):
        cv2.setTrackbarPos("h_min", "img_contourBox", 7)
        cv2.setTrackbarPos("h_max", "img_contourBox", 30)
        cv2.setTrackbarPos("s_min", "img_contourBox", 20)
        cv2.setTrackbarPos("s_max", "img_contourBox", 140)
        cv2.setTrackbarPos("v_min", "img_contourBox", 190)
        cv2.setTrackbarPos("v_max", "img_contourBox", 250)
        cv2.setTrackbarPos("blur", "img_contourBox", 9)
        cv2.setTrackbarPos("g_scale", "img_contourBox", 100)




capture.release()
cv2.destroyAllWindows()