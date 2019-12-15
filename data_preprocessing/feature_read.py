import numpy as np

path = './features/'


def feature_read():
    features = np.loadtxt(path + 'feature5.txt')
    labels = np.loadtxt(path + 'label.txt')
    return features, labels


if __name__ == '__main__':
    feature_read()
