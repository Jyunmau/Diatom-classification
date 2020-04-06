import abc
import numpy as np


class FeatureInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_feature(self, image: np.ndarray):
        pass

    @abc.abstractmethod
    def split_num(self):
        pass
