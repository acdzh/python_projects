import cv2
import numpy as np

#img = cv2.imread("C:\\Users\\acdzh\\Desktop\\Python\\opencv\\lena.jpg")
def threshBar(x):
   pass

img = cv2.imread("C:\\Users\\acdzh\\Desktop\\Python\\opencv\\1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Binary Image', thresh)

# 使用形态学运算滤除噪点
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# 靠近目标中心的是前景 远离目标中心的是背景 硬币边缘是未知区域
# 确定背景
sure_bg = cv2.dilate(opening,kernel,iterations=3)
cv2.imshow('Background Image', sure_bg)

# 确定前景
# 使用距离转换让硬币之间分开
# 如果只是单纯抠前景 则可以不使用距离变换
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv2.imshow('Foreground Image', sure_fg)

# 确定未知区域
# 背景图减去前景图得到未知区域
# 类似于同心圆中大圆减去小圆得到圆环 圆环就是未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow('Unknown', unknown)

# 从0开始进行标记
# 这个函数可以将各个连通域从0开始标号 同一个连通域的像素的标签相同
ret, markers = cv2.connectedComponents(sure_fg)

# 因为0是未知区域 所有标签自增1
markers = markers+1

# 标记未知区域 这里unknown中的白色的环状区域为未知区域
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
cv2.imshow('Result Image', img)

cv2.waitKey()
cv2.destroyAllWindows()