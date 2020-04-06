import cv2
import numpy


class SiftFeature:
    dest = None
    split_num = None

    def calculate_sift(self, img):
        sift = cv2.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(img, None)
        self.dest = des

    def get_sift_feature(self, img):
        self.calculate_sift(img)
        print(self.dest.shape)
        self.split_num = self.dest[1].shape[0]
        return self.dest[1]

    def get_split_num(self):
        return self.split_num
