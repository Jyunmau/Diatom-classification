import abc

import numpy as np
import core.path_some as ps


##todo: 处理batch的问题

class FeatureReadInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_feature(self, image: np.ndarray):
        pass


class FeatureRead(FeatureReadInterface):
    def get_feature(self, image: np.ndarray):
        pass

    @staticmethod
    def feature_read(data_set_num: int, feature_code: str):
        cls = ps.PathSome()
        features = np.loadtxt(cls.fetch(data_set_num, feature_code, 'feature'))
        labels = np.loadtxt(cls.fetch(data_set_num, '', 'label'))
        return features, labels


if __name__ == '__main__':
    feature_read()
