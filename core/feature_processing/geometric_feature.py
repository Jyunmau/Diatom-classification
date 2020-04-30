import cv2
import numpy as np

np.set_printoptions(suppress=True)


class GeometricFeatures:
    """提取几何特征"""

    split_num = None

    def contours(self, gray_img):
        """
        提取矩形度、延长度、周长比、似圆度、形状复杂性
        :param gray_img:
        :return:
        """
        gray_img = 255 - gray_img
        _, binary_img = cv2.threshold(gray_img, maxval=255, thresh=2, type=cv2.THRESH_BINARY)
        # 找物体边界
        _, contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 最大物体边界，以确认是目标物体硅藻
        area = []
        for i in range(len(contours)):
            area.append(cv2.contourArea(contours[i]))
        cnt = contours[area.index(max(area))]
        # 计算各参数
        db_area = np.fabs(cv2.contourArea(cnt))
        db_length = cv2.arcLength(cnt, True)
        rect = cv2.minAreaRect(cnt)
        rect_width, rect_height = rect[1]
        rectangularity = db_area / (rect_width * rect_height)
        extension = rect_width / rect_height
        perimeter_ratio = 2 * (rect_width + rect_height) / db_length
        roundness = 4 * np.pi * db_area / (db_length * db_length)
        shape_complexity = (db_length * db_length) / db_area
        return np.array([rectangularity, extension, perimeter_ratio, roundness, shape_complexity])

    def hu_moments(self, gray_img):
        """
        提取7个hu不变矩
        :param gray_img:
        :return:
        """
        gray_img = 255 - gray_img
        moments = cv2.moments(gray_img)
        m = np.array([moments['m11'], moments['m12'],
                      moments['m02'], moments['m20'], moments['m21'], moments['m30'], moments['m03']])
        # print(m.shape)
        humoments = cv2.HuMoments(moments)
        return np.concatenate([humoments[:2].flatten(), m])

    def get_geometric_features(self, gray_img):
        cont = self.contours(gray_img)
        hu = self.hu_moments(gray_img)
        features = np.concatenate([cont, hu])
        self.split_num = features.shape[0]
        return features

    def get_split_num(self):
        return self.split_num
