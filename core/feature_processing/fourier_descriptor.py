import cv2
import numpy as np


class FourierDescriptorFeature:
    """傅里叶描述子"""
    gray_image = None
    binary_image = None
    image_contour = None
    fd = None

    def __init__(self, img):
        self.gray_image = img

    def binary_morphology(self):
        """二值化&形态学闭操作"""
        ret2, th2 = cv2.threshold(self.gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
        th2 = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel, (-1. - 1), 2)
        self.binary_image = th2

    def extract_contour(self):
        """取得目标轮廓"""
        contours, hier = cv2.findContours(self.binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        area = []
        for i in range(len(contours)):
            area.append(cv2.contourArea(contours[i]))
        max_idx = np.argmax(area)
        self.binary_image = cv2.drawContours(self.binary_image, contours[max_idx], -1, (255, 255, 255), 1, 8, hier)
        self.image_contour = contours[max_idx]

    def calculate_fourier_descriptor(self):
        """计算傅里叶描述子"""
        s = len(self.image_contour)
        f = []
        for u in range(s):
            sum_x = 0
            sum_y = 0
            for j in range(s):
                p = self.image_contour[j]
                x = p.x
                y = p.y
                sum_x += (x * np.cos(2 * np.pi * u * j / s) + y * np.sin(2 * np.pi * u * j / s))
                sum_y += (y * np.cos(2 * np.pi * u * j / s) - x * np.sin(2 * np.pi * u * j / s))
            f.append(np.sqrt((sum_x * sum_x) + (sum_y * sum_y)))
        fd = []
        fd.append(np.float(0))
        for k in range(2, 17):
            f[k] = f[k] / f[1]
            fd.append(f[k])
        self.fd = fd
        return fd

    def get_fourier_descriptor(self):
        """调用接口"""
        self.binary_morphology()
        self.extract_contour()
        self.calculate_fourier_descriptor()
        return self.fd
