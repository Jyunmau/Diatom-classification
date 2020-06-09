"""
@File : image_read.py
@Time : 2020/06/09 13:51:23
@Author : Jyunmau
@Version : 1.0
"""

import abc

import cv2
import configparser
import glob
import numpy as np

from core.path_some import PathSome as ps


class ImageReadInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_image(self, *v):
        pass

    @abc.abstractmethod
    def image_preprocessing(self, *v):
        pass


class ImageRead(ImageReadInterface):
    """图像的读取和预处理"""

    def get_image(self, file_path: str, data_set_num: int = 2, is_cvt2gray=True, is_preprocess=True):
        """
        读取图像并转为灰度图, 大小统一到1024*1024
        :param is_preprocess: 是否需要对图片做预处理
        :param file_path: 图片的路径
        :param data_set_num: 数据集编号，2是新建的
        :param is_cvt2gray: 是否将读取的图像转为灰度图输出
        :return: 图像
        """
        gray_image = None
        if not data_set_num == 0:
            image = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        else:
            image = file_path
        if is_cvt2gray and len(image.shape) == 3:
            grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            grayimg = cv2.resize(grayimg, (1024, 1024))
            grayimg = cv2.medianBlur(grayimg, 5)
            # 这里是处理上届数据集的白色底问题
            if data_set_num == 1:
                grayimg = 255 - grayimg
            gray_image = grayimg
        else:
            gray_image = image
        if is_preprocess:
            gray_image = self.image_preprocessing(gray_image)
        return gray_image

    def image_preprocessing(self, image):
        """
        对读取出的图像做预处理，这里做了中值滤波
        :param image: 单张图像
        :return: 处理后的图像
        """
        img = cv2.medianBlur(image, (5, 5), 0)
        # img = cv2.GaussianBlur(image, (5, 5), 0)
        return img


if __name__ == "__main__":
    img_read = ImageRead()
