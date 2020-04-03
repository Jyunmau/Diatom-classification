# Embedded：随机森林
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor

# 加载波士顿房价作为数据集
boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]

# n_estimators为森林中树木数量，max_depth树的最大深度
rf = RandomForestRegressor(n_estimators=20, max_depth=4)
scores = []
for i in range(X.shape[1]):
    # 每次选择一个特征，进行交叉验证，训练集和测试集为7:3的比例进行分配，
    # ShuffleSplit()函数用于随机抽样（数据集总数，迭代次数，test所占比例）
    score = cross_val_score(rf, X[:, i:i + 1], Y, scoring="r2",
                            cv=ShuffleSplit(len(X), 3, .3))
    scores.append((round(np.mean(score), 3), names[i]))

# 打印出各个特征所对应的得分
print(sorted(scores, reverse=True))

# Embedded：基于树模型的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier

# GBDT作为基模型的特征选择
SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)

# wrapper：递归特征消除法
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# 递归特征消除法，返回特征选择后的数据
# 参数estimator为基模型
# 参数n_features_to_select为选择的特征个数
RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)

# 卡方检验
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# 选择K个最好的特征，返回选择特征后的数据
SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)
