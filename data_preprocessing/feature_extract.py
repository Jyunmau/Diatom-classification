import image_processing.image_read as imread
import image_processing.image_feature as imfeature
import image_processing.image_feature2 as imfeature2
import image_processing.image_segmentation as imseg
from sklearn import svm
import numpy as np

path = '../features/'


def feature_extract():
    images, labels = imread.image_read()
    features = []
    for image in images[:2]:
        gbf = imfeature.GlcmBasedFeature()
        texture = gbf.get_glcm_features(image)
        # texture = imfeature2.glgcm(image)
        gf = imfeature.GeometricFeatures()
        geometric = gf.get_geometric_features(image)
        feature = np.concatenate([texture, geometric])
        features.append(feature)
    features = np.array(features)
    labels = np.array(labels, dtype=np.int)
    print(features.shape)
    print(labels.shape)
    # test_images, test_labels = imread.image_read(data_type='test')
    # test_features = []
    # for image in test_images:
    #     gbf = imfeature.GlcmBasedFeature()
    #     texture = gbf.get_glcm_features(image)
    #     # texture = imfeature2.glgcm(image)
    #     gf = imfeature.GeometricFeatures()
    #     geometric = gf.get_geometric_features(image)
    #     feature = np.concatenate([texture, geometric])
    #     test_features.append(feature)
    # test_features = np.array(test_features)
    # test_labels = np.array(test_labels, dtype=np.int)
    # print(test_features.shape)
    # print(test_labels.shape)
    # X = np.concatenate([features, test_features])
    # Y = np.concatenate([labels, test_labels])
    # print(X.shape)
    # print(Y.shape)
    # np.savetxt(path + "feature3.txt", X)
    # np.savetxt(path + "label3.txt", Y)


if __name__ == '__main__':
    feature_extract()
