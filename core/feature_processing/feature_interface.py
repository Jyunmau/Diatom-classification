# todo：这个文件完成特征提取器接口
import abc


class FeatureInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_feature(self):
        pass
