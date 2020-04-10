import abc
import core.image_processing.image_read as imread
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
import core.image_processing.image_segmentation as imseg
import core.data_preprocessing.PCA_processing as pca
import core.data_preprocessing.feature_read as fr
import core.data_preprocessing.data_set_read as dsr
import core.public_signal as ps

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
import numpy as np
from sklearn.externals import joblib

from sklearn.neural_network import MLPClassifier


class ImageClassifierInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fit(self):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def predict(self):
        pass


class ImageClassifier(ImageClassifierInterface):
    def __init__(self, feature_read: fr.FeatureReadInterface, data_set_read: dsr.DataSetReadInterface
                 , model_type: str = 'svm', is_scaler: bool = True, is_pca: bool = False,
                 is_find_best_suparam: bool = False, is_save_model=True):
        self.clf = None
        self.model_type = model_type
        self.is_scaler = is_scaler
        self.is_pca = is_pca
        self.is_find_best_suparam = is_find_best_suparam
        self.is_save_model = is_save_model
        self.feature_read = feature_read
        self.data_set_read = data_set_read
        self.train_image_path = None
        self.test_image_path = None
        self.model = None

    def set_model_type(self, model_type: str):
        self.model_type = model_type

    def set_is_scaler(self, is_scaler: bool):
        self.is_scaler = is_scaler

    def set_is_pca(self, is_pca: bool):
        self.is_pca = is_pca

    def set_is_find_best_suparam(self, is_find_best_suparam: bool):
        self.is_find_best_suparam = is_find_best_suparam

    def set_is_save_model(self, is_save_model: bool):
        self.is_save_model = is_save_model

    def save(self):
        joblib.dump(self.clf, "models/" + self.model_type + '_' + str(
            self.data_set_read.data_set_num) + '_' + self.feature_read.feature_code + '.m')

    def load(self):
        self.model = joblib.load("models/" + self.model_type + '_' + str(
            self.data_set_read.data_set_num) + '_' + self.feature_read.feature_code + '.m', self.clf)

    def predict(self):
        if self.test_image_path is None:
            self.test_image_path = self.data_set_read.get_data()['images']
        features, labels = self.feature_read.get_feature_label(self.data_set_read)
        self.load()
        results = self.model.predict(features)
        public_signal = ps.PublicSignal()
        for i in range(len(results)):
            public_signal.send_signal_predict_result(labels[i], results[i], self.test_image_path[i])
            yield labels[i], results[i], self.test_image_path[i]

    def fit(self):
        features, labels = self.feature_read.get_feature_label(self.data_set_read)
        print(features.shape)
        print(labels.shape)
        ss = StratifiedShuffleSplit(n_splits=1, test_size=0.25, train_size=0.75, random_state=0)
        train_index, test_index = next(ss.split(features, labels))
        image_path = self.data_set_read.get_data()['images']
        train_features, train_labels = features[train_index], labels[train_index]
        test_features, test_labels = features[test_index], labels[test_index]
        self.train_image_path = np.array(image_path)[train_index]
        self.test_image_path = np.array(image_path)[test_index]
        if self.is_pca:
            features = pca.pca_reduce(features)
        if self.is_scaler:
            scaler = StandardScaler()
            scaler.fit(train_features)
            train_features = scaler.transform(train_features)
            test_features = scaler.transform(test_features)
        # print(labels)
        # labels = labels.reshape((labels.shape[0], 1))
        # # labels = labels.reshape((labels.shape[0]))
        # # print(labels.shape)
        # rand_f_l = np.concatenate((features, labels), axis=1)
        # rand_f_l = shuffle(rand_f_l)
        # labels = rand_f_l[:, -1]
        # features = rand_f_l[:, :-1]
        # print(features)
        print(features.shape)
        print(labels.shape)
        if self.is_find_best_suparam:
            parameters = {
                'svc__gamma': [0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.04, 0.05, 0.06, 0.08, 0.09, 0.1, 0.11, 0.3,
                               0.5, 1],
                'svc__C': [0.001, 0.01, 0.1, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 15, 16, 17, 18, 20, 22]}
            clf = Pipeline([('ss', StandardScaler()), ('svc', SVC())])
            # clf = Pipeline([('svc', SVC())])
            gs = GridSearchCV(clf, parameters, refit=True, cv=10, verbose=1, n_jobs=-1)
            gs.fit(train_features, train_labels)  # Run fit with all sets of parameters.
            print('最优参数: ', gs.best_params_)
            print('最佳性能: ', gs.best_score_)
        else:
            clf = None
            if self.model_type == 'ann':
                clf = MLPClassifier(solver='sgd', activation='relu', alpha=1e-4, hidden_layer_sizes=(20, 50),
                                    random_state=1, verbose=10, learning_rate_init=.1, max_iter=500)
            elif self.model_type == 'knn':
                clf = KNeighborsClassifier()
            elif self.model_type == 'svm':
                clf = SVC(C=2, gamma=0.009)
            clf.fit(train_features, train_labels)
            self.clf = clf
            print("\n>>====== train finished with %s samples ======<<\n" % train_labels.shape[0])
            if self.is_save_model:
                self.save()
                print('>>====== model saved ! ======<<')
            print('>>======train_set score:======<<')
            print("acc:%s" % clf.score(train_features, train_labels))
            predicted = clf.predict(train_features)
            print("Confusion matrix:\n%s" % metrics.confusion_matrix(train_labels, predicted))
            print('\n>>======test_set score:======<<')
            print("acc:%s" % clf.score(test_features, test_labels))
            predicted = clf.predict(test_features)
            # print("Classification report for classifier %s:\n%s\n"
            #       % (clf, metrics.classification_report(expected, predicted)))
            print("Confusion matrix:\n%s" % metrics.confusion_matrix(test_labels, predicted))
            self.print_confusion_matrix(metrics.confusion_matrix(test_labels, predicted))

    def print_confusion_matrix(self, cm):
        import matplotlib.pyplot as plt
        import numpy as np

        # labels表示你不同类别的代号，比如这里的demo中有13个类别
        labels = ["Coscinodiscus", "Cyclotella", "Diatome", "Melosira", "Navicula",
                  "Nitzschia", "Stephanodiscus", "Synedra", "Thalassiosira"]

        tick_marks = np.array(range(len(labels))) + 0.5

        def plot_confusion_matrix(cm, title='Confusion Matrix', cmap=plt.cm.binary):
            plt.imshow(cm, interpolation='nearest', cmap=cmap)
            plt.title(title)
            plt.colorbar()
            xlocations = np.array(range(len(labels)))
            plt.xticks(xlocations, labels, rotation=30)
            plt.yticks(xlocations, labels)
            plt.ylabel('True label')
            plt.xlabel('Predicted label')

        cm = cm
        np.set_printoptions(precision=2)
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        plt.figure(figsize=(12, 17), dpi=90)

        ind_array = np.arange(len(labels))
        x, y = np.meshgrid(ind_array, ind_array)

        for x_val, y_val in zip(x.flatten(), y.flatten()):
            c = cm_normalized[y_val][x_val]
            if c > 0.01:
                plt.text(x_val, y_val, "%0.2f" % (c,), color='red', fontsize=7, va='center', ha='center')
        # offset the tick
        plt.gca().set_xticks(tick_marks, minor=True)
        plt.gca().set_yticks(tick_marks, minor=True)
        plt.gca().xaxis.set_ticks_position('none')
        plt.gca().yaxis.set_ticks_position('none')
        plt.grid(True, which='minor', linestyle='-')
        plt.gcf().subplots_adjust(bottom=0.17, left=0.17)

        plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix')
        plt.show()
