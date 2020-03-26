import abc

import numpy as np
import core.path_some as ps
import core.data_preprocessing.data_set_read as dsr


class FeatureReadInterface(metaclass=abc.ABCMeta):
    data_set_num: int
    feature_code: str

    @abc.abstractmethod
    def get_feature_label(self, data_set_read: dsr.DataSetReadInterface, batch_num: int = 0):
        pass


class FeatureRead(FeatureReadInterface):
    feature_code = '110001'

    def set_feature_code(self, geometric_feature: bool, glcm_feature: bool, fourier_descriptor_feature: bool,
                         hog_feature: bool, sift_feature: bool, lbp_feature: bool):
        res = ''
        if geometric_feature:
            res += '1'
        else:
            res += '0'
        if glcm_feature:
            res += '1'
        else:
            res += '0'
        if fourier_descriptor_feature:
            res += '1'
        else:
            res += '0'
        if hog_feature:
            res += '1'
        else:
            res += '0'
        if sift_feature:
            res += '1'
        else:
            res += '0'
        if lbp_feature:
            res += '1'
        else:
            res += '0'
        self.feature_code = res

    def get_feature_label(self, data_set_read: dsr.DataSetReadInterface, batch_num: int = 0):
        data_set_num = data_set_read.data_set_num
        self.feature_code = self.feature_code
        cls = ps.PathSome()
        features = np.loadtxt(cls.fetch(data_set_num, self.feature_code, 'feature'))
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
