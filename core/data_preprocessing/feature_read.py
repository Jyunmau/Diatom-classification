import numpy as np
import core.path_some as ps

path = './features/'


# TODO(仅读取单个文件，路径处理提出来)

def feature_read(data_set_num: int, feature_num: int):
    cls = ps.PathSome()
    features = np.loadtxt(cls.fetch(data_set_num, feature_num, 'feature'))
    labels = np.loadtxt(cls.fetch(data_set_num, feature_num, 'label'))
    return features, labels


if __name__ == '__main__':
    feature_read()
