# 将rgb图片转换为bgr
import cv2
 
imgpath = "/Users/duzhongqiang/Desktop/uav3.jpg"
saveimg = r"/Users/duzhongqiang/Desktop/uav3.bgr"
 
img = cv2.imread(imgpath)
save_img_size = 416
 
if img is None:
    print("img is none")
else:
    img = cv2.resize(img,(save_img_size,save_img_size))
    (B, G, R) = cv2.split(img)
    with open(saveimg,'wb')as fp:
        for i in range(save_img_size):
            for j in range(save_img_size):
                fp.write(B[i, j])
        for i in range(save_img_size):
            for j in range(save_img_size):
                fp.write(G[i, j])
        for i in range(save_img_size):
            for j in range(save_img_size):
                fp.write(R[i, j])
 
    print("save success")