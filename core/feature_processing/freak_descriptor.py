import cv2
import numpy as np
import core.feature_processing.feature_interface as fi
import core.image_processing.image_read as imr


class FreakDescriptorFeature(fi.FeatureInterface):
    def get_feature(self, image: np.ndarray):
        freakExtractor = cv2.xfeatures2d.FREAK_create()
        hessianThreshold = 20000
        surfDetector = cv2.xfeatures2d_SURF.create(hessianThreshold)
        keypoints = surfDetector.detect(image)
        keypoints, descriptors = freakExtractor.compute(image, keypoints)
        del freakExtractor
        return descriptors.flatten()


if __name__ == '__main__':
    image = imr.ImageRead().get_image(
        '/Users/jyunmau/PycharmProjects/Diatom-classification/images/img4seg/Cyanobacteria_6.png', 2)
    fdf = FreakDescriptorFeature()
    des = fdf.get_feature(image)
    print(des.shape)
