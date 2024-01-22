import numpy as np
import cv2 as cv

#Import image tulips.jpg
tulips = cv.imread('tulips.jpg')
tulips = cv.resize(tulips,(500,300))

#Create kernel with 1's on the diagonals, then divide by 9 for average
img_kernel = np.array([[1,0,0,0,1],[0,1,0,1,0], [0,0,1,0,0], [0,1,0,1,0],[1,0,0,0,1]]) 
img_kernel = img_kernel/9

flt_img = cv.filter2D(tulips,-1,img_kernel)

cv.imshow('Diagonal_Filter', flt_img)

cv.waitKey(0) 
cv.destroyAllWindows()