"""
@File : data_read.py
@Time : 2020/06/09 16:14:49
@Author : Jyunmau
@Version : 1.0
"""

import abc

import numpy as np
import core.data_preprocessing.data_set_read as dsr


class DataReadInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_images_iter(self, *v):
        pass

    @abc.abstractmethod
    def get_labels(self, *v):
        pass


class DataRead(DataReadInterface):
    """处理数据的读取问题"""

    def get_images_iter(self, data_set_read: dsr.DataSetReadInterface):
        """
        获得图片路径的iter对象（cifar为图片本身的iter）
        :return: iter对象
        """
        if data_set_read.data_set_num == 0:
            data = data_set_read.get_data()
            images = [np.uint8(img.reshape(3, 32, 32).transpose(1, 2, 0).astype('float')) for img in data['images']]
        else:
            images = data_set_read.get_data()['images']
        # 上层返回信息判断
        if images is None:
            raise ValueError('images object is None, check class DataSetRead for more info.')
        else:
            for image in images:
                yield image

    def get_labels(self, data_set_read: dsr.DataSetReadInterface):
        """
        返回labels信息
        :return: 一个str的list，每一个元素是一个label
        """
        data = data_set_read.get_data()
        return data['labels']
