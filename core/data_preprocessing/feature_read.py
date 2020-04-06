import abc

import numpy as np
import core.path_some as ps
import core.data_preprocessing.data_set_read as dsr
import core.data_preprocessing.feature_selection as fs
import core.data_preprocessing.feature_preproc as fp


class FeatureReadInterface(metaclass=abc.ABCMeta):
    data_set_num: int
    feature_code: str

    @abc.abstractmethod
    def get_feature_label(self, data_set_read: dsr.DataSetReadInterface, batch_num: int = 0):
        pass


class FeatureRead(FeatureReadInterface):
    feature_code = '110001'
    selection_func = 'filter'
    k = 450
    is_regularize: bool = True
    is_normalize: bool = True
    is_transform: bool = True

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

    def set_selection_func(self, selection_func):
        self.selection_func = selection_func

    def set_k(self, k):
        self.k = k

    def set_is_regularize(self, is_regularize):
        self.is_regularize = is_regularize

    def set_is_normalize(self, is_normalize):
        self.is_normalize = is_normalize

    def set_is_transform(self, is_transform):
        self.is_transform = is_transform

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
        feature_batch = np.array(feature_batch)
        label_batch = np.array(label_batch)
        split_list = cls.get_feature_split(self.feature_code)
        feature_batch = fp.transform(feature_batch, split_list)
        feature_batch = fs.transform(feature_batch, label_batch, k=self.k, selection_func=self.selection_func)
        return feature_batch, label_batch


if __name__ == '__main__':
    fbr = FeatureRead()
    f, b = fbr.get_feature_label(2, '110001', 0)
    print(f)
