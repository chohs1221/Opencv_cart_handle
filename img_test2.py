import cv2
import numpy as np

# bgr -> hsv, mask
def mask(bgr, low, high):
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    low_color = np.array([low[0], low[1], low[2]])
    high_color = np.array([high[0], high[1], high[2]])
    img_mask = cv2.inRange(hsv, low_color, high_color)

    return cv2.bitwise_and(bgr, bgr, mask = img_mask)

if __name__ == "__main__":
    src = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    low = [7, 30, 150]
    high = [30, 90, 250]
    img_masked = mask(src, low, high)
    cv2.imshow("img_masked", img_masked)

    cv2.waitKey()
    cv2.destroyAllWindows()