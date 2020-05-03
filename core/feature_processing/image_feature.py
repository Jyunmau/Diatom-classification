import abc
import time

import cv2
from sklearn.preprocessing import StandardScaler

import core.path_some as ps
import core.image_processing.image_read as imr
import core.data_preprocessing.data_set_read as dsr
import core.feature_processing.geometric_feature as gmt_feature
import core.feature_processing.glcm_based_feature as glcm_feature
import core.feature_processing.fourier_descriptor as fd_feature
import core.feature_processing.hog_feature as hog_feature
import core.feature_processing.sift_feature as sift_feature
import core.feature_processing.lbp_feature as lbp_feature

from PySide2.QtCore import QObject, Signal

import core.public_signal as public_signal

import numpy as np


# class ImageFeatureInterface(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def fetch_proc(self, image_it, img_read: imr.ImageReadInterface, data_set_num: int):
#         pass


class ImageFeature(QObject):
    label_id = {"Coscinodiscus": "0", "Cyclotella": "1", "Diatome": "2", "Melosira": "3", "Navicula": "4",
                "Nitzschia": "5", "Stephanodiscus": "6", "Synedra": "7", "Thalassiosira": "8"}
    features = []
    labels = []

    def __init__(self, geometric_feature: bool = True, glcm_feature: bool = True,
                 fourier_descriptor_feature: bool = False, hog_feature: bool = False,
                 sift_feature: bool = False, lbp_feature: bool = True, is_scale_1by1: bool = True):
        super(ImageFeature, self).__init__()
        self.geometric_feature = geometric_feature
        self.glcm_feature = glcm_feature
        self.fourier_descriptor_feature = fourier_descriptor_feature
        self.hog_feature = hog_feature
        self.sift_feature = sift_feature
        self.lbp_feature = lbp_feature
        self.public_signal = public_signal.PublicSignal()
        self.proc = None
        self.public_signal.signal_rewrite_choose.connect(self._set_proc)
        self.is_scale_1by1 = is_scale_1by1

    def _set_proc(self, choose: str):
        self.proc = choose

    def _get_feature_code(self):
        res = ''
        if self.geometric_feature:
            res += '1'
        else:
            res += '0'
        if self.glcm_feature:
            res += '1'
        else:
            res += '0'
        if self.fourier_descriptor_feature:
            res += '1'
        else:
            res += '0'
        if self.hog_feature:
            res += '1'
        else:
            res += '0'
        if self.sift_feature:
            res += '1'
        else:
            res += '0'
        if self.lbp_feature:
            res += '1'
        else:
            res += '0'
        self.feature_code = res
        return res

    def _resolve_feature_code(self, feature_code: str):
        if feature_code[0] == '1':
            self.geometric_feature = True
        else:
            self.geometric_feature = False
        if feature_code[1] == '1':
            self.glcm_feature = True
        else:
            self.glcm_feature = False
        if feature_code[2] == '1':
            self.fourier_descriptor_feature = True
        else:
            self.fourier_descriptor_feature = False
        if feature_code[3] == '1':
            self.hog_feature = True
        else:
            self.hog_feature = False
        if feature_code[4] == '1':
            self.sift_feature = True
        else:
            self.sift_feature = False
        if feature_code[5] == '1':
            self.lbp_feature = True
        else:
            self.lbp_feature = False

    def setter_feature_code(self, geo: bool, glcm: bool, fd: bool, hog: bool, sift: bool, lbp: bool):
        self.geometric_feature = geo
        self.glcm_feature = glcm
        self.fourier_descriptor_feature = fd
        self.hog_feature = hog
        self.sift_feature = sift
        self.lbp_feature = lbp

    def _setter_geometric_feature(self, is_feature: bool):
        self.geometric_feature = is_feature

    def _setter_glcm_feature(self, is_feature: bool):
        self.glcm_feature = is_feature

    def _setter_lbp_feature(self, is_feature: bool):
        self.lbp_feature = is_feature

    def _setter_hog_feature(self, is_feature: bool):
        self.hog_feature = is_feature

    def _setter_sift_feature(self, is_feature: bool):
        self.sift_feature = is_feature

    def _setter_fourier_descriptor_feature(self, is_feature: bool):
        self.fourier_descriptor_feature = is_feature

    def fetch_proc(self, img_it, img_read: imr.ImageReadInterface, data_set_read: dsr.DataSetReadInterface):
        self._get_feature_code()
        cls = ps.PathSome()
        self.labels = data_set_read.get_data()['labels']
        if cls.is_file_exists(data_set_read.data_set_num, self.feature_code, 'feature'):
            print("this feature combination has been fetched, do you want to rewrite it ?")
            self.public_signal.send_rewrite()
            while self.proc is None:
                continue
            # proc = input("y / n :")
            if self.proc == 'y':
                cls.delete_file(data_set_read.data_set_num, self.feature_code, 'feature')
            else:
                return
        split_list = []
        self.features.clear()
        while True:
            try:
                imgfile = next(img_it)
                print(imgfile)
                self.public_signal.send_image_path(imgfile)
                image = img_read.get_image(imgfile, data_set_read.data_set_num)
                feature = None
                if self.geometric_feature:
                    gf = gmt_feature.GeometricFeatures()
                    geometric = gf.get_geometric_features(image)
                    split_list.append(str(gf.get_split_num()))
                    if feature is None:
                        feature = geometric
                    else:
                        feature = np.concatenate([feature, geometric])
                if self.glcm_feature:
                    gbf = glcm_feature.GlcmBasedFeature()
                    texture = gbf.get_glcm_features(image)
                    split_list.append(str(gbf.get_split_num()))
                    if feature is None:
                        feature = texture
                    else:
                        feature = np.concatenate([feature, texture])
                if self.fourier_descriptor_feature:
                    fdf = fd_feature.FourierDescriptorFeature()
                    fourier = fdf.get_fourier_descriptor(image)
                    split_list.append(str(fdf.get_split_num()))
                    if feature is None:
                        feature = fourier
                    else:
                        feature = np.concatenate([feature, fourier])
                if self.hog_feature:
                    # 自实现的hog
                    # hogf = hog_feature.Hog_descriptor(image, cell_size=8, bin_size=8)
                    # hog_vector, _ = hogf.extract()
                    # hog_hist = np.histogram(np.array(hog_vector))
                    # hog = hog_hist.flatten()
                    # cv的hog
                    hog = hog_feature.hog_compute(image)
                    hog = np.array(hog).flatten()
                    split_list.append(str(hog_feature.get_split_num()))
                    if feature is None:
                        feature = hog
                    else:
                        feature = np.concatenate([feature, hog])
                if self.sift_feature:
                    sf = sift_feature.SiftFeature()
                    sift = sf.get_sift_feature(image)
                    split_list.append(str(sf.get_split_num()))
                    if feature is None:
                        feature = sift
                    else:
                        feature = np.concatenate([feature, sift])
                if self.lbp_feature:
                    # lbp = lbp_feature.LBP(image)
                    lbp_f = lbp_feature.LbpFeature()
                    lbp = lbp_f.get_lbp_feature(image)
                    split_list.append(str(lbp_f.get_split_num()))
                    if feature is None:
                        feature = lbp
                    else:
                        feature = np.concatenate([feature, lbp])

                self.features.append(feature)
                # self.labels.append(label)
            except StopIteration:
                break
        cls.fetch_feature_split(self.feature_code, split_list)
        features = np.array(self.features)
        labels = np.array(self.labels, dtype=np.int)
        print('>>>>===============================<<<<')
        print('特征提取完成！，文件已保存')
        print(features.shape)
        print(labels.shape)
        print(features.shape)
        print(labels.shape)
        if not cls.is_file_exists(data_set_read.data_set_num, self.feature_code, 'feature'):
            np.savetxt(cls.fetch(data_set_read.data_set_num, self.feature_code, 'feature'), features, fmt="%s")
        if not cls.is_file_exists(data_set_read.data_set_num, '', 'label'):
            np.savetxt(cls.fetch(data_set_read.data_set_num, '', 'label'), labels)
        print('特征提取完成！，文件已保存')
        self.public_signal.send_finished()


if __name__ == "__main__":
    img_f = ImageFeature(False, False, False, True, False, False)
    img_f.fetch_proc()
