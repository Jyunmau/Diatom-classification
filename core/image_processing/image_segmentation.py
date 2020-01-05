import cv2
import numpy as np
from skimage import img_as_ubyte
from core.image_processing import image_read as imgr


def strokEdges(blurKsize=7, edgeKsize=5):
    # img = imgr.image_read()
    # grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图
    gray_images, _ = imgr.image_read()
    for grayimg in gray_images:
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


if __name__ == "__main__":
    strokEdges()
