import numpy as np

path = './features/'


# TODO(仅读取单个文件，路径处理提出来)

def feature_read():
    features = np.loadtxt(path + 'feature4.txt')
    labels = np.loadtxt(path + 'label.txt')
    return features, labels


if __name__ == '__main__':
    feature_read()
