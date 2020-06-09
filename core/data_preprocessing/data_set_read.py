"""
@File : data_set_read.py
@Time : 2020/06/09 16:15:01
@Author : Jyunmau
@Version : 1.0
"""

import abc
import glob
import os

import numpy as np
import core.path_some as ps

max_data_set_num = 2


class DataSetReadInterface(metaclass=abc.ABCMeta):
    @property
    def data_set_num(self):
        return self._data_set_num

    @data_set_num.setter
    def data_set_num(self, value):
        if not isinstance(value, int):
            raise ValueError('data_set_num must be an integer!')
        if value < 0 or value > max_data_set_num:
            raise ValueError('data_set_num out of range!')
        self._data_set_num = value

    def __init__(self, path_some: ps.PathSome, data_set_num: int = 2):
        """
        :param data_set_num: 数据集编号
        :param path_some: 用于提供路径的单例对象
        """
        self.data_set_num = data_set_num
        self.path_some = path_some

    def set_data_set_num(self, data_set_num: int):
        self.data_set_num = data_set_num

    @abc.abstractmethod
    def get_data(self):
        pass


class DataSetRead(DataSetReadInterface):
    """处理用于特征提取的各数据集的读取"""
    label_id = {"Coscinodiscus": 0, "Cyclotella": 1, "Diatome": 2, "Melosira": 3, "Navicula": 4,
                "Nitzschia": 5, "Stephanodiscus": 6, "Synedra": 7, "Thalassiosira": 8}

    def get_data(self):
        """
        根据数据集编号获取数据集
        :return: 字典，images和labels分别是一个list，对应图片链接和标签号
        """
        path = self.path_some.img(self.data_set_num)
        if self.data_set_num == 0:
            return self._standard_set(path)
        elif self.data_set_num == 1:
            return self._1_set(path)
        elif self.data_set_num == 2:
            return self._2_set(path)
        else:
            return

    def _standard_set(self, path):
        """由于cifar-10数据集的特殊性，这里返回的images是image的flattened列表"""

        def unpickle(file):
            import pickle
            with open(file, 'rb') as fo:
                data_dict = pickle.load(fo, encoding='bytes')
            return data_dict[b'data'], data_dict[b'labels']

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
        img_path = glob.glob(path + '/' + '*' + '/stage_1/*' + 'png')
        labels = [self.label_id[img_file.split('/')[4]] for img_file in img_path]
        data = {'images': img_path, 'labels': labels}
        return data


if __name__ == '__main__':
    import core.path_some as ps

    ops = ps.PathSome()
    dsr = DataSetRead(0, ops)
    print(dsr.get_data()['images'].shape)
