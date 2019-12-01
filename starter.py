import image_processing.image_read as imread
import image_processing.image_feature as imfeature
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
import image_processing.image_segmentation as imseg
import data_preprocessing.feature_read as fr
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
import numpy as np


def main():
    features, labels = fr.feature_read()
    # labels = labels.reshape((labels.shape[0],1))
    # # labels = labels.reshape((labels.shape[0]))
    # # print(labels.shape)
    # rand_f_l = np.concatenate((features, labels), axis=1)
    # rand_f_l = shuffle(rand_f_l)
    # labels = rand_f_l[:,-1]
    # features = rand_f_l[:,:-1]
    # # print(features)
    # # print(features.shape)
    # # print(labels.shape)
    # # print(rand_f_l.shape)

    parameters = {'svc__gamma': [0.008, 0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.05, 0.08, 0.09, 0.1, 0.11, 1],
                  'svc__C': [0.001, 0.01, 0.1, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 15, 16, 17, 18, 20]}
    clf = Pipeline([('ss', StandardScaler()), ('svc', SVC())])
    gs = GridSearchCV(clf, parameters, refit=True, cv=5, verbose=1, n_jobs=-1)
    gs.fit(features, labels)  # Run fit with all sets of parameters.
    print('最优参数: ', gs.best_params_)
    print('最佳性能: ', gs.best_score_)


if __name__ == '__main__':
    main()
