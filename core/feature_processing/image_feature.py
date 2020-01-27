import cv2

import core.path_some as ps
import core.image_processing.image_read as imr
import core.feature_processing.geometric_feature as imfeature

import numpy as np


def fetch_proc():
    cls = ps.PathSome()
    img_it = cls.img()
    features = []
    labels = []
    while True:
        try:
            imgfile = next(img_it)
            image = imr.image_read(imgfile)
            label = imgfile.split('\\')[1]
            gbf = imfeature.GlcmBasedFeature()
            texture = gbf.get_glcm_features(image)
            # texture = imfeature2.glgcm(image)
            gf = imfeature.GeometricFeatures()
            geometric = gf.get_geometric_features(image)
            # hog = imfeature3.Hog_descriptor(image, cell_size=8, bin_size=8)
            # hog_vector, _ = hog.extract()
            # hog_hist = np.histogram(np.array(hog_vector))
            # hog_vector = hog_hist.flatten()
            # hog = imfeature3.hog_compute(image)
            # hog = np.array(hog).flatten()
            # feature = np.concatenate([texture, geometric])
            feature = texture
            # print(feature)
            # feature = hog
            features.append(feature)
            labels.append(label)
        except StopIteration:
            break
    features = np.array(features)
    labels = np.array(labels, dtype=np.int)
    print(features.shape)
    print(labels.shape)
    print(features.shape)
    print(labels.shape)
    np.savetxt(cls.fetch_path(6), features)
    # np.savetxt(path + "label5.txt", labels)
    # TODO(可选何种特征)
    # TODO(保存文件特征，类别)
    # TODO(处理多进程问题)
    pass


if __name__ == "__main__":
    fetch_proc()
