# -*- coding:utf-8 -*-
import glob
import os
import numpy as np


# 单例模式的装饰器

class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class PathSome(object):
    """
    花式获取项目各类文件路径
    """

    img_path = None
    images = 'H:/硅藻图像库/硅藻分类（张雨）/图像集'
    images1 = 'H: / 硅藻图像库 / 图像集'
    image_segmentation = 'H:/硅藻图像库/综合'
    data_set_1 = '/Volumes/其它/图像集/'
    data_set_2 = '/Volumes/其它/edited/'
    data_set_standard = '/Volumes/其它/cifar-10-batches-py/'
    features = '/Users/jyunmau/PycharmProjects/Diatom-classification/features'
    models = '/Users/jyunmau/PycharmProjects/Diatom-classification/models'

    # features = 'C:\\Users\\JyunmauChan\\Documents\\GitHub\\Diatom-classification\\features'
    # models = 'C:\\Users\\JyunmauChan\\Documents\\GitHub\\Diatom-classification\\models'

    def __init__(self):
        self.fetch_path = glob.glob(self.features + '/' + '*' + 'txt')
        self.seg_path = glob.glob(self.image_segmentation + '/' + '*' + '/*' + 'jpg')

    def img(self, data_set_num: int):
        if data_set_num == 0:
            return self.data_set_standard
        elif data_set_num == 1:
            return self.data_set_1
        elif data_set_num == 2:
            return self.data_set_2
        else:
            pass

    def seg_img(self):
        for image in self.seg_path:
            yield image

    def fetch(self, data_set_num: int, s_n: str, f_or_l):
        fetch_path = self.features + '/' + 'ds' + str(data_set_num) + '_' + f_or_l + s_n + '.txt'
        return fetch_path

    def mod(self, s_n=''):
        mod_path = self.models + '/' + 'model' + str(s_n) + '.cvs'
        return mod_path

    def is_file_exists(self, data_set_num: int, s_n: str, f_or_l):
        fetch_path = self.features + '/' + 'ds' + str(data_set_num) + '_' + f_or_l + s_n + '.txt'
        ife = os.path.exists(fetch_path)
        return ife

    def delete_file(self, data_set_num: int, s_n: str, f_or_l):
        fetch_path = self.features + '/' + 'ds' + str(data_set_num) + '_' + f_or_l + s_n + '.txt'
        os.remove(fetch_path)


if __name__ == '__main__':
    cls = PathSome()
