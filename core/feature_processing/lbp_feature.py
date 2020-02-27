import cv2
import numpy as np
import os
import math
import core.path_some as ps
import core.image_processing.image_read as imr


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
    # res.flatten()
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


class LbpFeature:
    lbp_img = None
    g_mapping = [
        0, 1, 2, 3, 4, 58, 5, 6, 7, 58, 58, 58, 8, 58, 9, 10,
        11, 58, 58, 58, 58, 58, 58, 58, 12, 58, 58, 58, 13, 58, 14, 15,
        16, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58,
        17, 58, 58, 58, 58, 58, 58, 58, 18, 58, 58, 58, 19, 58, 20, 21,
        22, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58,
        58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58,
        23, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58,
        24, 58, 58, 58, 58, 58, 58, 58, 25, 58, 58, 58, 26, 58, 27, 28,
        29, 30, 58, 31, 58, 58, 58, 32, 58, 58, 58, 58, 58, 58, 58, 33,
        58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 34,
        58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58,
        58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 35,
        36, 37, 58, 38, 58, 58, 58, 39, 58, 58, 58, 58, 58, 58, 58, 40,
        58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 41,
        42, 43, 58, 44, 58, 58, 58, 45, 58, 58, 58, 58, 58, 58, 58, 46,
        47, 48, 58, 49, 58, 58, 58, 50, 51, 52, 58, 53, 54, 55, 56, 57]

    def calculate_lbp_img(self, gray_image, radius: int = 2, count: int = 8):
        """计算lbp图谱"""
        dh = np.round([radius * math.sin(i * 2 * math.pi / count) for i in range(count)])
        dw = np.round([radius * math.cos(i * 2 * math.pi / count) for i in range(count)])
        height, width = gray_image.shape
        lbp = np.zeros(gray_image.shape, dtype=np.int)
        gray_image_1 = np.pad(gray_image, radius, 'edge')
        for k in range(count):
            h, w = int(radius + dh[k]), int(radius + dw[k])
            lbp += ((gray_image > gray_image_1[h:h + height, w:w + width]) << k)
        self.lbp_img = lbp
        return lbp

    def calculate_lbp_histogram(self, h_count=7, w_count=5, max_lbp_value=255):
        """分块计算lbp直方图"""
        height, width = self.lbp_img.shape
        res = np.zeros((h_count * w_count, max(self.g_mapping) + 1), dtype=np.float)
        assert (max_lbp_value + 1 == len(self.g_mapping))

        for h in range(h_count):
            for w in range(w_count):
                blk = self.lbp_img[int(height * h / h_count):int(height * (h + 1) / h_count),
                      int(width * w / w_count):int(width * (w + 1) / w_count)]
                hist1 = np.bincount(blk.ravel(), minlength=max_lbp_value)
                hist = res[h * w_count + w, :]
                for v, k in zip(hist1, self.g_mapping):
                    hist[k] += v
                hist /= hist.sum()
        return res

    def get_lbp_feature(self, gray_image):
        self.calculate_lbp_img(gray_image)
        res = self.calculate_lbp_histogram()
        return res


def normalize(data):
    m = np.mean(data)
    mx = np.max(data)
    mn = np.min(data)
    return [int(255 * (float(i) - m) / (mx - mn)) for i in data]


if __name__ == "__main__":
    cls = ps.PathSome(2)
    img_it = cls.img()
    imgfile = next(img_it)
    image = imr.image_read(imgfile, 2)
    lbp_f = LbpFeature()
    lbp_image = lbp_f.calculate_lbp_img(image)
    print(lbp_image.shape)
    print(lbp_image.dtype)
    print(np.argmax(lbp_image))
    dst = np.zeros(lbp_image.shape, dtype=np.float32)
    dst = cv2.normalize(lbp_image, dst=dst, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
    print(type(lbp_image))
    print(dst.shape)
    dst *= 255
    dst.astype(np.int16)
    np.uint8(dst)
    dst.dtype = 'uint8'
    cv2.namedWindow("lbp_img", 0)
    cv2.resizeWindow("lbp_img", 640, 640)
    cv2.imshow("lbp_img", dst)
    cv2.waitKey(0)
    lbp_hist = lbp_f.get_lbp_feature(image)
    print(lbp_hist.shape)
