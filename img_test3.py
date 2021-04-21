from img_test1 import *
from img_test2 import *

if __name__ == "__main__":
    src = cv2.imread("3.jpg", cv2.IMREAD_COLOR)
    src = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    height, width, channel = src.shape
    cv2.imshow("src", src)
    low = [7, 20, 160]
    high = [30, 140, 250]
    img_masked = mask(src, low, high)
    cv2.putText(img_masked, "h: ("+str(low[0])+", "+str(high[0])+")", (10, 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(img_masked, "s: ("+str(low[1])+", "+str(high[1])+")", (10, 25), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(img_masked, "v: ("+str(low[2])+", "+str(high[2])+")", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
    cv2.imshow("img_masked", img_masked)

    img_blur = Bluring(img_masked, 9)
    cv2.imshow('img_blur', img_blur)
    img_binary = Grayscale(img_blur, 100)
    cv2.imshow('img_binary', img_binary)
    contours, img_contour = draw_Contours(img_binary, height, width, channel)
    cv2.imshow('contours', img_contour)
    img_contourBox = draw_ContourBox(img_contour, contours, 300, 3, height, width, channel, src)
    cv2.imshow('img_contourBox', img_contourBox)

    cv2.waitKey()
    cv2.destroyAllWindows()
