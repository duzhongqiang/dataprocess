#修改图片大小
import cv2

img = cv2.imread("/Users/duzhongqiang/Desktop/00008.png")
size = img.shape
print(size)
img2 = cv2.resize(img, (416, 416))
size = img2.shape
print(size)
cv2.imwrite('/Users/duzhongqiang/Desktop/uav3.jpg',img2)
# cv2.imshow('a',img2)
# cv2.waitKey(0)
