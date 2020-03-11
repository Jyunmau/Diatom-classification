import cv2
import configparser
import glob
import numpy as np

from core.path_some import PathSome


class ImageRead(object):
    """图像的读取和预处理"""

    def image_read(self, file_path: str, data_set_num: int, is_cvt2gray=True):
        """
        读取图像并转为灰度图, 大小统一到1024*1024
        :param file_path: 图片的路径
        :param data_set_num: 数据集编号，2是新建的
        :param is_cvt2gray: 是否将读取的图像转为灰度图输出
        :return: 图像
        """
        image = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        if is_cvt2gray and len(image.shape) == 3:
            grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            grayimg = cv2.resize(grayimg, (1024, 1024))
            grayimg = cv2.medianBlur(grayimg, 5)
            # 这里是处理上届数据集的白色底问题
            if data_set_num == 1:
                grayimg = 255 - grayimg
            return grayimg
        else:
            return image

    def image_preprocessing(self, image):
        img = cv2.GaussianBlur(image, (5, 5), 0)
        return img


if __name__ == "__main__":
    img_read = ImageRead()
