"""
@File : image_segmentation.py
@Time : 2020/06/09 16:15:39
@Author : Jyunmau
@Version : 1.0
"""

import cv2
import numpy as np
from skimage import img_as_ubyte
import core.path_some as ps
import core.image_processing.image_read as imr


def strokEdges(blurKsize=7, edgeKsize=5):
    """
    硅藻图像ROI区域分割，弹窗显示原图及识别的ROI区域矩形线框
    :param blurKsize: 中值滤波的卷积核大小
    :param edgeKsize: 边缘检测的卷积核大小
    :return:
    """
    cls = ps.PathSome()
    img_it = cls.seg_img()
    while True:
        try:
            imgfile = next(img_it)
            grayimg = imr.image_read(imgfile)
            grayimg = cv2.GaussianBlur(grayimg, (5, 5), 0)
            equimg = cv2.equalizeHist(grayimg)  # 直方图均衡化
            # img_1 = cv2.adaptiveThreshold(equimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
            # 边缘检测
            if blurKsize >= 3:
                graySrc = cv2.medianBlur(equimg, blurKsize)
            else:
                graySrc = equimg
            cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)
            normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
            outimg = equimg * normalizedInverseAlpha
            outimg = outimg.astype(np.uint8)
            # outimg = cv2.adaptiveThreshold(outimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
            cv2.imshow("outimg", outimg)
            # 膨胀
            outimg = 255 - outimg
            kernel = np.ones((5, 5), np.uint8)
            outimg = cv2.dilate(outimg, kernel, iterations=1)
            outimg = cv2.adaptiveThreshold(outimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 10)
            outimg = 255 - outimg
            cv2.imshow("outimg", outimg)
            # 找最大连通区域的正外接矩形
            contours, hier = cv2.findContours(outimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            area = []
            for i in range(len(contours)):
                area.append(cv2.contourArea(contours[i]))
            max_idx = np.argmax(area)
            (x, y, w, h) = cv2.boundingRect(contours[max_idx])
            cv2.rectangle(grayimg, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.imshow("img2", grayimg)
            # cv2.imshow("grav", graySrc)
            # cv2.imshow("img_1", img_1)
            cv2.waitKey(1000)
        except StopIteration:
            break


if __name__ == "__main__":
    strokEdges()
