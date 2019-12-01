import cv2
import numpy as np

np.set_printoptions(suppress=True)


class GlcmBasedFeature:
    """提取基于灰度共生矩阵的纹理特征"""

    # 灰度共生矩阵
    ret = None

    def glcm(self, grayimg, d_x=2, d_y=2, gray_level=32):
        """
        求灰度共生矩阵（归一化）
        :param grayimg: 单通道灰度图像
        :param d_x: 另一点相对于当前点水平方向偏移量
        :param d_y: 另一点相对于当前点垂直方向偏移量
        :param gray_level: 归一化后的灰度级数
        :return: 该图像的归一化灰度共生矩阵
        """
        grayimg = 255 - grayimg
        max_gray = grayimg.max()
        height, width = grayimg.shape
        arr = grayimg.astype(np.float64)
        arr = arr * (gray_level - 1) // max_gray
        ret = np.zeros([gray_level, gray_level])
        for j in range(height - abs(d_y)):
            for i in range(width - abs(d_x)):
                rows = arr[j][i].astype(int)
                cols = arr[j + d_y][i + d_x].astype(int)
                ret[rows][cols] += 1
        if d_x >= d_y:
            ret = ret / float(height * (width - 1))
        else:
            ret = ret / float((height - 1) * (width - 1))
        self.ret = ret
        return ret

    def angular_second_moment(self):
        """
        计算角二阶矩，图像纹理均一规则时值大
        :param ret: 灰度共生矩阵
        :return: 角二阶矩
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        asm: np.float = 0.0
        for j in range(height):
            for i in range(width):
                asm += (self.ret[j][i] * self.ret[j][i])
        return asm

    def entropy(self):
        """
        计算熵，图像纹理复杂时值大
        （灰度共生矩阵值分布均等，即其随机性大）
        :param ret: 灰度共生矩阵
        :return: 熵
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        ent: np.float = 0.0
        for j in range(height):
            for i in range(width):
                if self.ret[j][i] == 0:
                    continue
                ent += self.ret[j][i] * np.log(self.ret[j][i])
        return -ent

    def contrast_ratio(self):
        """
        计算对比度，纹理越清晰值越大
        :param ret: 灰度共生矩阵
        :return: 对比度
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        con: np.float = 0.0
        for j in range(height):
            for i in range(width):
                con += self.ret[j][i] * np.square(j - i)
        return con

    def inverse_differential_moment(self):
        """
        计算反差分矩(逆方差)，纹理清晰规律性强值越大
        :param ret: 灰度共生矩阵
        :return: 反差分矩
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        idm: np.float = 0.0
        for j in range(height):
            for i in range(width):
                idm += self.ret[j][i] / (1 + np.square(j - i))
        return idm

    def get_glcm_features(self, grayimg):
        """
        获得四种基于灰度共生矩阵的纹理特征
        :param grayimg: 单通道灰度图像
        :return: 一行4列数组，纹理特征
        """
        self.glcm(grayimg)
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        features = np.zeros((4), np.float)
        features[0] = self.angular_second_moment()
        features[1] = self.contrast_ratio()
        features[2] = self.entropy()
        features[3] = self.inverse_differential_moment()
        return features


class GeometricFeatures:
    """提取几何特征"""

    def contours(self, gray_img):
        """
        提取矩形度、延长度、周长比、似圆度、形状复杂性
        :param gray_img:
        :return:
        """
        gray_img = 255 - gray_img
        _, binary_img = cv2.threshold(gray_img, maxval=255, thresh=2, type=cv2.THRESH_BINARY)
        # 找物体边界
        contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 最大物体边界，以确认是目标物体硅藻
        area = []
        for i in range(len(contours)):
            area.append(cv2.contourArea(contours[i]))
        cnt = contours[area.index(max(area))]
        # 计算傅里叶形状描述子

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
        return rectangularity, extension, perimeter_ratio, roundness, shape_complexity

    def fourier_descriptor(self, contour):
        pass

    def hu_moments(self, gray_img):
        """
        提取7个hu不变矩
        :param gray_img:
        :return:
        """
        moments = cv2.moments(gray_img)
        humoments = cv2.HuMoments(moments)
        return humoments[0]

    def get_geometric_features(self, gray_img):
        cont = self.contours(gray_img)
        hu = self.hu_moments(gray_img)
        features = np.zeros((6), np.float)
        features[:5] = np.array(list(cont))
        features[5:] = hu
        return features
