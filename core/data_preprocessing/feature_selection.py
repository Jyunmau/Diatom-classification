"""
@File : glcm_based_feature.py
@Time : 2020/06/09 13:50:39
@Author : Jyunmau
@Version : 1.0
"""

import numpy as np
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier
from sklearn.feature_selection import SelectFromModel, RFE, SelectKBest, chi2
from sklearn.linear_model import LogisticRegression


def transform(data, label, selection_func='filter', k=450):
    """
    特征筛选
    :param data: 样本特征，大小为(n_samples,n_features)
    :param label: 样本标签
    :param selection_func: 特征筛选所用的方法，可选填'embedded','wrapper','filter'
    :param k: 筛选后的特征维数
    :return: 筛选后得到的特征向量，'filter'会改变特征顺序
    """
    if selection_func == 'embedded':
        # Embedded：基于树模型的特征选择法
        # GBDT作为基模型的特征选择
        tran_data = SelectFromModel(GradientBoostingClassifier(), max_features=k).fit_transform(data, label)
        return tran_data
    elif selection_func == 'wrapper':
        # wrapper：递归特征消除法
        # 递归特征消除法，返回特征选择后的数据
        # 参数estimator为基模型
        # 参数n_features_to_select为选择的特征个数
        tran_data = RFE(estimator=LogisticRegression(), n_features_to_select=k).fit_transform(data, label)
        return tran_data
    elif selection_func == 'filter':
        # filter卡方检验
        # 选择K个最好的特征，返回选择特征后的数据
        tran_data = SelectKBest(chi2, k=k).fit_transform(data, label)
        return tran_data
    elif selection_func == 'embedded_scores':
        # Embedded：随机森林
        names = []
        # n_estimators为森林中树木数量，max_depth树的最大深度
        rf = RandomForestRegressor(n_estimators=20, max_depth=4)
        scores = []
        for i in range(data.shape[1]):
            # 每次选择一个特征，进行交叉验证，训练集和测试集为7:3的比例进行分配，
            # ShuffleSplit()函数用于随机抽样（数据集总数，迭代次数，test所占比例）
            score = cross_val_score(rf, data[:, i:i + 1], label, scoring="r2",
                                    cv=ShuffleSplit(len(data), 3, .3))
            scores.append((round(np.mean(score), 3), names[i]))
        # 打印出各个特征所对应的得分
        print(sorted(scores, reverse=True))
