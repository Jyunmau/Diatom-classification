"""
@File : feature_preproc.py
@Time : 2020/06/09 16:05:40
@Author : Jyunmau
@Version : 1.0
"""

from sklearn.preprocessing import StandardScaler, Normalizer, PolynomialFeatures, FunctionTransformer
from numpy import log1p
import numpy as np


def transform(feature, split_list=None, is_regularize: bool = True, is_normalize: bool = True,
              is_transform: bool = True):
    """
    对特征进行预处理
    :param is_regularize: 是否对特征进行正则化
    :param is_normalize: 是否对特征进行归一化
    :param is_transform: 是否对特征进行多项式变换（默认对第一类特征扩增）
    :param feature: 组合好的特征矩阵，1D是样本数，2D是特征维数
    :param split_list: 一个list, 元素是按照特征顺序依次放置的各特征维数
    :return: 预处理完成的特征矩阵
    """
    if split_list is None:
        split_list = [18]
    if is_transform:
        feature = np.concatenate(
            [feature, PolynomialFeatures().fit_transform(feature[:, :split_list[0]])[:, split_list[0]:]], axis=1)
    if is_regularize:
        feature = StandardScaler().fit_transform(feature)
    if is_normalize:
        feature = Normalizer().fit_transform(feature)
    return feature


if __name__ == "__main__":
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    a = transform(a)
    print(a)
