import cv2

import core.path_some as ps
import core.image_processing.image_read as imr
import core.feature_processing.geometric_feature as gmt_feature
import core.feature_processing.glcm_based_feature as glcm_feature
import core.feature_processing.fourier_descriptor as fd_feature
import core.feature_processing.hog_feature as hog_feature
import core.feature_processing.sift_feature as sift_feature
import core.feature_processing.lbp_feature as lbp_feature

import numpy as np


class ImageFeature:
    label_id = {"Coscinodiscus": "0", "Cyclotella": "1", "Diatome": "2", "Melosira": "3", "Navicula": "4",
                "Nitzschia": "5", "Stephanodiscus": "6", "Synedra": "7", "Thalassiosira": "8"}
    features = []
    labels = []

    def __init__(self, geometric_feature: bool, glcm_feature: bool, fourier_descriptor_feature: bool, hog_feature: bool,
                 sift_feature: bool, lbp_feature: bool, data_set_num: int):
        self.geometric_feature = geometric_feature
        self.glcm_feature = glcm_feature
        self.fourier_descriptor_feature = fourier_descriptor_feature
        self.hog_feature = hog_feature
        self.sift_feature = sift_feature
        self.lbp_feature = lbp_feature
        self.data_set_num = data_set_num

    def feature_code(self):
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
        return res

    def fetch_proc(self):
        cls = ps.PathSome(self.data_set_num)
        if cls.is_file_exists(self.data_set_num, self.feature_code(), 'feature'):
            # todo: ui要处理这个选择
            print("this feature combination has been fetched, do you want to rewrite it ?")
            proc = input("y / n :")
            if proc == 'y':
                cls.delete_file(self.data_set_num, self.feature_code(), 'feature')
            else:
                return
        img_it = cls.img()
        while True:
            try:
                imgfile = next(img_it)
                image = imr.image_read(imgfile, self.data_set_num)
                if self.data_set_num == 1:
                    label = imgfile.split('/')[5]
                else:
                    label = self.label_id[imgfile.split('/')[4]]
                feature = None
                if self.geometric_feature:
                    gf = gmt_feature.GeometricFeatures()
                    geometric = gf.get_geometric_features(image)
                    if feature is None:
                        feature = geometric
                    else:
                        feature = np.concatenate([feature, geometric])
                if self.glcm_feature:
                    gbf = glcm_feature.GlcmBasedFeature()
                    texture = gbf.get_glcm_features(image)
                    if feature is None:
                        feature = texture
                    else:
                        feature = np.concatenate([feature, texture])
                if self.fourier_descriptor_feature:
                    fdf = fd_feature.FourierDescriptorFeature()
                    fourier = fdf.get_fourier_descriptor(image)
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
                    if feature is None:
                        feature = hog
                    else:
                        feature = np.concatenate([feature, hog])
                if self.sift_feature:
                    sf = sift_feature.SiftFeature()
                    sift = sf.get_sift_feature(image)
                    if feature is None:
                        feature = sift
                    else:
                        feature = np.concatenate([feature, sift])
                if self.lbp_feature:
                    # lbp = lbp_feature.LBP(image)
                    lbp_f = lbp_feature.LbpFeature()
                    lbp = lbp_f.get_lbp_feature(image)
                    if feature is None:
                        feature = lbp
                    else:
                        feature = np.concatenate([feature, lbp])

                self.features.append(feature)
                self.labels.append(label)
            except StopIteration:
                break
        features = np.array(self.features)
        labels = np.array(self.labels, dtype=np.int)
        print(features.shape)
        print(labels.shape)
        print(features.shape)
        print(labels.shape)
        if not cls.is_file_exists(self.data_set_num, self.feature_code(), 'feature'):
            np.savetxt(cls.fetch(self.data_set_num, self.feature_code(), 'feature'), features)
        if not cls.is_file_exists(self.data_set_num, '', 'label'):
            np.savetxt(cls.fetch(self.data_set_num, '', 'label'), labels)


if __name__ == "__main__":
    img_f = ImageFeature(False, False, False, True, False, False, 2)
    img_f.fetch_proc()
