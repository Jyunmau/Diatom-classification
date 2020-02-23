import cv2
import numpy


class SiftFeature:
    dest = None

    def calculate_sift(self, img):
        sift = cv2.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(img, None)
        self.dest = des

    def get_sift_feature(self, img):
        self.calculate_sift(img)
        return self.dest[1]
