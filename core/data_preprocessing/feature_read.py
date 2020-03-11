import numpy as np
import core.path_some as ps


##todo: 处理batch的问题

def feature_read(data_set_num: int, feature_code: str):
    cls = ps.PathSome()
    features = np.loadtxt(cls.fetch(data_set_num, feature_code, 'feature'))
    labels = np.loadtxt(cls.fetch(data_set_num, '', 'label'))
    return features, labels


if __name__ == '__main__':
    feature_read()
