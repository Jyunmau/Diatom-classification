import image_processing.image_read as imread
import image_processing.geometric_feature as imfeature
import image_processing.image_feature2 as imfeature2
import image_processing.hog_feature as imfeature3
import image_processing.image_segmentation as imseg
from sklearn import svm
import numpy as np

path = '../features/'


# TODO(与image_feature合并，修改todo见image_feature)

def feature_extract():
    images, labels = imread.image_read()
    features = []
    for image in images:
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
        feature = np.concatenate([texture, geometric])
        # print(feature)
        # feature = hog
        features.append(feature)
    features = np.array(features)
    labels = np.array(labels, dtype=np.int)
    print(features.shape)
    print(labels.shape)
    test_images, test_labels = imread.image_read(data_type='test')
    test_features = []
    for image in test_images:
        gbf = imfeature.GlcmBasedFeature()
        texture = gbf.get_glcm_features(image)
        # texture = imfeature2.glgcm(image)
        gf = imfeature.GeometricFeatures()
        geometric = gf.get_geometric_features(image)
        # hog = imfeature3.hog_compute(image)
        # hog = np.array(hog).flatten()
        feature = np.concatenate([texture, geometric])
        # feature = hog
        test_features.append(feature)
    test_features = np.array(test_features)
    test_labels = np.array(test_labels, dtype=np.int)
    print(test_features.shape)
    print(test_labels.shape)
    X = np.concatenate([features, test_features])
    Y = np.concatenate([labels, test_labels])
    print(X.shape)
    print(Y.shape)
    np.savetxt(path + "feature5.txt", X)
    # np.savetxt(path + "label5.txt", Y)


if __name__ == '__main__':
    feature_extract()
