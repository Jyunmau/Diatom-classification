import cv2
import configparser
import glob
import numpy as np

path = '../config.cfg'


def image_read(file_path: str, is_cvt2gray=True):
    """
    读取图像并转为灰度图, 大小统一到1024*1024
    :param is_cvt2gray: 是否将读取的图像转为灰度图输出
    :return: 图像
    """
    image = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    # and len(image.shape) == 3
    if is_cvt2gray and len(image.shape) == 3:
        grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayimg = cv2.resize(grayimg, (1024, 1024))
        grayimg = cv2.medianBlur(grayimg, 5)
        # 这里是处理上届数据集的白色底问题
        # FIXME(新图像库做好后把这里反相去掉)
        grayimg = 255 - grayimg
        return grayimg
    else:
        return image


if __name__ == "__main__":
    image_read()