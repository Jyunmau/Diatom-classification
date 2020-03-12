import abc


class ImageClassifierInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fit(self):
        pass


class ImageClassifier(ImageClassifierInterface):
    def fit(self):
        pass
