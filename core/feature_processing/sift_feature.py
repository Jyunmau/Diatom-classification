import cv2
import numpy


class SiftFeature:
    gray_image = None
    dest = None

    def __init__(self, img):
        self.gray_image = img

    def calculate_sift(self):
        sift = cv2.SIFT()
        kp, des = sift.detectAndCompute(self.gray_image, None)
        self.dest = des

    def get_sift_feature(self):
        return self.dest[1]
