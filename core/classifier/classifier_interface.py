# todo：这个文件完成分类器接口
import abc


class ClassifierInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def train(self):
        pass
