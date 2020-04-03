from sklearn.preprocessing import StandardScaler, Normalizer, PolynomialFeatures, FunctionTransformer
from numpy import log1p
import numpy as np


def transform(feature, code=None):
    """
    对特征进行预处理
    :param feature: 组合好的特征矩阵，1D是样本数，2D是特征维数
    :param code: 一个list, 元素是按照特征顺序依次放置的各特征维数
    :return: 预处理完成的特征矩阵
    """
    if code is None:
        code = [18]
    feature = np.concatenate([feature, PolynomialFeatures().fit_transform(feature[:, :2])[:, 2:]], axis=1)
    feature = StandardScaler().fit_transform(feature)
    feature = Normalizer().fit_transform(feature)
    return feature


if __name__ == "__main__":
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    a = transform(a)
    print(a)
