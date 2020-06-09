import abc


class ClassifierInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def train(self):
        pass
