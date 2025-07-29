import cv2 as cv

img = cv.imread('images/images3.jpeg')
img = cv.convertScaleAbs(img)
#cv.namedWindow('Orig', cv.WINDOW_NORMAL)
cv.imshow('Orig', img)

lab_bgr = cv.cvtColor(img, cv.COLOR_LAB2BGR)
#cv.namedWindow('RGB --> LAB',cv.WINDOW_NORMAL)
#cv.imshow('RGB --> LAB', lab_bgr)

gray = cv.cvtColor(lab_bgr,cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.namedWindow('Adaptive Thresholding', cv.WINDOW_AUTOSIZE)
cv.imshow('Adaptive Thresholding', adaptive_thresh)


adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 11)
cv.namedWindow('Adaptive Thresholding inv', cv.WINDOW_AUTOSIZE)
cv.imshow('Adaptive Thresholding inv', adaptive_thresh_inv)
# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)