import abc

import numpy as np
import core.path_some as ps


##todo: 处理batch的问题

class FeatureReadInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_feature_label(self, data_set_num: int, feature_code: str):
        pass


class FeatureRead(FeatureReadInterface):
    # def __init__(self, path_some: ps.PathSome):
    #     self.path_some = path_some
    @staticmethod
    def get_feature_label(data_set_num: int, feature_code: str, batch_num: int = 5):
        cls = ps.PathSome()
        features = np.loadtxt(cls.fetch(data_set_num, feature_code, 'feature'))
        labels = np.loadtxt(cls.fetch(data_set_num, '', 'label'))
        if batch_num == 0:
            return features, labels
        feature_it = iter(features)
        label_it = iter(labels)
        feature_batch = [[] for _ in range(batch_num)]
        label_batch = [[] for _ in range(batch_num)]
        count = 0
        while True:
            try:
                feature = next(feature_it)
                label = next(label_it)
                feature_batch[count].append(feature)
                label_batch[count].append(label)
                count = (count + 1 if (count < batch_num - 1) else 0)
            except StopIteration:
                break
        return np.array(feature_batch), np.array(label_batch)


if __name__ == '__main__':
    fbr = FeatureRead()
    f, b = fbr.get_feature_label(2, '110001', 0)
    print(f)
