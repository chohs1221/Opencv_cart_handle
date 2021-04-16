import cv2
import numpy as np



# 블러링
def Bluring(img, kernel_size):
    img_blur = cv2.blur(img, (kernel_size, kernel_size), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
    #cv2.imshow('blur', img_blur)
    return img_blur
# 그레이스케일
def Grayscale(img, thresh):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)
    #cv2.imshow('binary', binary)
    return binary
# 컨투어
def draw_Contours(img, height, width, channel):
    contours, _ = cv2.findContours(
        img, 
        mode=cv2.RETR_LIST, 
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    cv2.drawContours(temp_result, contours=contours, contourIdx=-1, color=(255, 255, 255))
    #cv2.imshow('contours', temp_result)
    return contours, temp_result
# 컨투어 박스
def draw_ContourBox(img, contours, min_width, min_ratio, height, width, channel, src):
    temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    contours_dict = []
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        if max(rect[1][0], rect[1][1]) > min_width and max(rect[1][0]/rect[1][1], rect[1][1]/rect[1][0]) > min_ratio:
            box = cv2.boxPoints(rect)
            box = np.int0(box) 
            cv2.drawContours(src, [box], -1, (0, 255, 0), 2)
            cv2.putText(src, "("+str(box[0][1])+", "+str(box[0][0])+")", (box[0][0], box[0][1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(src, "("+str(box[1][1])+", "+str(box[1][0])+")", (box[1][0], box[1][1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(src, "("+str(box[3][1])+", "+str(box[3][0])+")", (box[3][0], box[3][1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(src, "("+str(box[2][1])+", "+str(box[2][0])+")", (box[2][0], box[2][1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            print("==========================================================")
            print("(x, y) = ({0})\n(width, height) = {1}\n(angle) = {2}".format(rect[0], rect[1], rect[2]))
            print(box)

        
            
    #cv2.imshow('result', temp_result)
    return src

if __name__ == "__main__":
    img = cv2.imread('5.jpg')
    height, width, channel = img.shape
    cv2.imshow('original', img)

    img_blur = Bluring(img, 15)
    cv2.imshow('img_blur', img_blur)
    img_binary = Grayscale(img_blur, 170)
    cv2.imshow('img_binary', img_binary)
    contours, img_contour = draw_Contours(img_binary, height, width, channel)
    cv2.imshow('contours', img_contour)
    img_contourBox = draw_ContourBox(img_contour, contours, 300, 3, height, width, channel)
    cv2.imshow('img_contourBox', img_contourBox)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
