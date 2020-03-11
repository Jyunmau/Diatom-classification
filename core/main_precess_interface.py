import abc
import numpy as np


class MainProcessInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_feature(self, image: np.ndarray):
        pass
