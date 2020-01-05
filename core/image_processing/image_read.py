import cv2
import configparser
import glob
import numpy as np

from core.path_some import PathSome

path = '../config.cfg'


def image_read(is_cvt2gray=True, file_type='jpg', data_type='train'):
    """
    获取数据
    读取图像并转为灰度图, 大小统一到1024*1024
    :param is_cvt2gray: 是否将读取的图像转为灰度图输出
    :param file_type: 图像后缀
    :param data_type: 选择输出训练集还是测试集
    :return: 图像数组，每个元素是一幅图像
            标签数组，下标对应图像
    """
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8-sig")
    cls = PathSome()
    imgfiles = cls.seg_img()
    images = []
    labels = []
    for imgfile in imgfiles:
        image = cv2.imdecode(np.fromfile(imgfile, dtype=np.uint8), -1)
        label = imgfile.split('\\')[1]
        if is_cvt2gray and len(image.shape) == 3:
            grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            grayimg = cv2.resize(grayimg, (1024, 1024))
            grayimg = cv2.medianBlur(grayimg, 5)
            images.append(grayimg)
            labels.append(label)
        else:
            images.append(image)
            labels.append(label)
    return images, labels


if __name__ == "__main__":
    image_read()
