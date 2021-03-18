from img_test1 import *
from img_test2 import *

if __name__ == "__main__":
    src = cv2.imread("2.jpg", cv2.IMREAD_COLOR)
    height, width, channel = src.shape
    low = [7, 20, 160]
    high = [30, 140, 250]
    img_masked = mask(src, low, high)
    cv2.imshow("img_masked", img_masked)

    img_blur = Bluring(img_masked, 9)
    cv2.imshow('img_blur', img_blur)
    img_binary = Grayscale(img_blur, 100)
    cv2.imshow('img_binary', img_binary)
    contours, img_contour = draw_Contours(img_binary, height, width, channel)
    cv2.imshow('contours', img_contour)
    img_contourBox = draw_ContourBox(img_contour, contours, 300, 3, height, width, channel)
    cv2.imshow('img_contourBox', img_contourBox)

    cv2.waitKey()
    cv2.destroyAllWindows()
