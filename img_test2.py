import cv2
import numpy as np

def h_filter(h, min_, max_):
    h = np.array(h)
    h_mask1 = min_<h
    h_mask2 = h<max_
    h_mask = h_mask1 & h_mask2
    h_ = h * h_mask
    return h_

def s_filter(s, min_, max_):
    s = np.array(s)
    s_mask1 = min_<s
    s_mask2 = s<max_
    s_mask = s_mask1 & s_mask2
    s_ = s * s_mask
    return s_

def v_filter(v, min_, max_):
    v = np.array(v)
    v_mask1 = min_<v
    v_mask2 = v<max_
    v_mask = v_mask1 & v_mask2
    v_ = v * v_mask
    return v_

if __name__ == "__main__":
    src = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    #dst = src[180:190, 500:520].copy()
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h_ = h_filter(h, 7, 30)
    s_ = s_filter(s, 45, 70)
    v_ = v_filter(v, 175, 240)
    
    hsv = cv2.merge([h_, s_, v_])
    cv2.imshow("result", hsv)



    cv2.waitKey()
    cv2.destroyAllWindows()