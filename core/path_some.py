# -*- coding:utf-8 -*-
import glob


# 单例模式的装饰器
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class PathSome(object):
    """
    花式获取项目各类文件路径
    """

    SegTest = '../ data - images / img4seg /'
    images = 'H:/硅藻图像库/硅藻分类（张雨）/图像集'
    images1 = 'H: / 硅藻图像库 / 图像集'
    image_segmentation = 'H:/硅藻图像库/综合'
    data_set_2 = '/Volumes/其它/edited'
    features = '/Users/jyunmau/PycharmProjects/Diatom-classification/features'
    models = '/Users/jyunmau/PycharmProjects/Diatom-classification/models'

    # features = 'C:\\Users\\JyunmauChan\\Documents\\GitHub\\Diatom-classification\\features'
    # models = 'C:\\Users\\JyunmauChan\\Documents\\GitHub\\Diatom-classification\\models'

    def __init__(self):
        self.img_path = glob.glob(self.data_set_2 + '/' + '*' + '/*/*' + 'png')
        self.fetch_path = glob.glob(self.features + '/' + '*' + 'txt')
        self.seg_path = glob.glob(self.image_segmentation + '/' + '*' + '/*' + 'jpg')
        # self.seg_path.append(glob.glob(self.image_segmentation + '/' + '*' + '/*' + 'png'))
        # print(self.img_path[0])
        # print(len(self.seg_path))

    def img(self):
        for image in self.img_path:
            yield image

    def seg_img(self):
        for image in self.seg_path:
            yield image

    def fetch(self, data_set_num: int, s_n: int, f_or_l):
        fetch_path = self.features + '/' + 'ds' + str(data_set_num) + '_' + f_or_l + str(s_n) + '.txt'
        return fetch_path

    def mod(self, s_n=''):
        mod_path = self.models + '/' + 'model' + str(s_n) + '.cvs'
        return mod_path


if __name__ == '__main__':
    cls = PathSome()
    str1 = cls.img()
    print(str1)
    str1 = cls.img()
    print(str1)
