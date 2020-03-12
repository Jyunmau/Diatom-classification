import abc

import numpy as np
import core.data_preprocessing.data_set_read as dsr


class DataReadInterface(metaclass=abc.ABCMeta):
    def __init__(self, data_set: dsr.DataSetReadInterface):
        self.data_set = data_set

    @abc.abstractmethod
    def get_images_iter(self):
        pass

    @abc.abstractmethod
    def get_labels(self):
        pass


class DataRead(DataReadInterface):
    """处理数据的读取问题"""

    def get_images_iter(self):
        """
        获得图片路径的iter对象（cifar为图片本身的iter）
        :return: iter对象
        """
        if self.data_set.data_set_num == 0:
            data = self.data_set.get_data()
            images = [np.uint8(img.reshape(3, 32, 32).transpose(1, 2, 0).astype('float')) for img in data['images']]
        else:
            images = self.data_set.get_data()['images']
        # 上层返回信息判断
        if images is None:
            raise ValueError('images object is None, check class DataSetRead for more info.')
        else:
            for image in images:
                yield image

    def get_labels(self):
        """
        返回labels信息
        :return: 一个str的list，每一个元素是一个label
        """
        data = self.data_set.get_data()
        return data['labels']
