import cv2
import numpy as np
import os


def LBP(image):
    W, H = image.shape  # 获得图像长宽
    xx = [-1, 0, 1, 1, 1, 0, -1, -1]
    yy = [-1, -1, -1, 0, 1, 1, 1, 0]  # xx, yy 主要作用对应顺时针旋转时,相对中点的相对值.
    res = np.zeros((W - 2, H - 2), dtype="uint8")  # 创建0数组,显而易见维度原始图像的长宽分别减去2，并且类型一定的是uint8,无符号8位,opencv图片的存储格式.
    for i in range(1, W - 2):
        for j in range(1, H - 2):
            temp = ""
            for m in range(8):
                Xtemp = xx[m] + i
                Ytemp = yy[m] + j  # 分别获得对应坐标点
                if image[Xtemp, Ytemp] > image[i, j]:  # 像素比较
                    temp = temp + '1'
                else:
                    temp = temp + '0'
            # print int(temp, 2)
            res[i - 1][j - 1] = int(temp, 2)  # 写入结果中
    return res


def Tran(src, drc):
    list = os.listdir(src)
    sum = 0
    for i in list:
        try:
            img = cv2.imread(src + "/" + i, 0)
            img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)  # 将图片变成固定大小224,224,这步可以不用,自己选择
            cv2.imshow("temp", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            res = LBP(img.copy())
            cv2.imwrite(drc + "/" + i, res)
            sum = int(sum) + 1
            print(i + " is finnished, number is " + str(sum))
        except:
            print("error in " + i)


src = "/home/rui/ttt/val"
drc = "/home/rui/ttt/end"

Tran(src, drc)
