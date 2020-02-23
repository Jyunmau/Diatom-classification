import core.image_processing.image_read as imread
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
import core.image_processing.image_segmentation as imseg
import core.data_preprocessing.PCA_processing as pca
import core.data_preprocessing.feature_read as fr
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
import numpy as np

from sklearn.neural_network import MLPClassifier


def main():
    features, labels = fr.feature_read(2, '000010')
    # features = pca.pca_reduce(features)
    print(labels)
    labels = labels.reshape((labels.shape[0], 1))
    # labels = labels.reshape((labels.shape[0]))
    # print(labels.shape)
    rand_f_l = np.concatenate((features, labels), axis=1)
    rand_f_l = shuffle(rand_f_l)
    labels = rand_f_l[:, -1]
    features = rand_f_l[:, :-1]
    # print(features)
    # print(features.shape)
    # print(labels.shape)
    # print(rand_f_l.shape)

    parameters = {
        'svc__gamma': [0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.04, 0.05, 0.06, 0.08, 0.09, 0.1, 0.11, 0.3, 0.5, 1],
        'svc__C': [0.001, 0.01, 0.1, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 15, 16, 17, 18, 20, 22]}
    clf = Pipeline([('ss', StandardScaler()), ('svc', SVC())])
    # clf = Pipeline([('svc', SVC())])
    gs = GridSearchCV(clf, parameters, refit=True, cv=10, verbose=1, n_jobs=-1)
    gs.fit(features, labels)  # Run fit with all sets of parameters.
    print('最优参数: ', gs.best_params_)
    print('最佳性能: ', gs.best_score_)

    # clf = MLPClassifier(solver='sgd', activation='relu', alpha=1e-4, hidden_layer_sizes=(20, 50), random_state=1
    #                     , verbose=10, learning_rate_init=.1, max_iter=500)
    # clf.fit(features, labels)
    # print(clf.score(features, labels))


if __name__ == '__main__':
    main()
