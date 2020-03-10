# todo: 这个文件要处理读取图片和标签的问题
import glob
import os

import numpy as np
import core.path_some as ps

max_data_set_num = 2


class DataSetRead(object):
    """处理用于特征提取的各数据集的读取"""
    label_id = {"Coscinodiscus": "0", "Cyclotella": "1", "Diatome": "2", "Melosira": "3", "Navicula": "4",
                "Nitzschia": "5", "Stephanodiscus": "6", "Synedra": "7", "Thalassiosira": "8"}

    @property
    def data_set_num(self):
        return self._data_set_num

    @data_set_num.setter
    def data_set_num(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > max_data_set_num:
            raise ValueError('score must between 0 ~ 100!')
        self.data_set_num = value

    def __init__(self, data_set_num):
        self._data_set_num = data_set_num

    def get_data(self, path_some: ps.PathSome):
        """
        根据数据集编号获取数据集
        :param data_set_num: 数据集编号
        :param path_some: PathSome类对象,用于提供路径
        :return: 字典，images和labels分别是一个list，对应图片链接和标签号
        """
        path = path_some.img(self._data_set_num)
        if self._data_set_num == 0:
            return self._standard_set(path)
        elif self._data_set_num == 1:
            return self._1_set(path)
        elif self._data_set_num == 2:
            return self._2_set(path)
        else:
            return

    def _standard_set(self, path):
        def unpickle(file):
            import pickle
            with open(file, 'rb') as fo:
                data_dict = pickle.load(fo, encoding='bytes')
            return data_dict['data'], data_dict['label']

        xs = []
        ys = []
        for b in range(1, 6):
            f = os.path.join(path, 'data_batch_%d' % (b,))
            data_train, label_train = unpickle(f)
            xs.append(data_train)
            ys.append(label_train)
        data_test, label_test = unpickle(os.path.join(path, 'test_batch'))
        xs.append(data_test)
        ys.append(label_test)
        data = {'images': np.concatenate(xs), 'labels': np.concatenate(ys)}
        return data

    def _1_set(self, path):
        img_path = glob.glob(path + '/' + '*' + '/*/*' + 'jpg')
        labels = [img_file.split('/')[5] for img_file in img_path]
        data = {'images': img_path, 'labels': labels}
        return data

    def _2_set(self, path):
        img_path = glob.glob(path + '/' + '*' + '/*/*' + 'png')
        labels = [self.label_id[img_file.split('/')[4]] for img_file in img_path]
        data = {'images': img_path, 'labels': labels}
        return data
