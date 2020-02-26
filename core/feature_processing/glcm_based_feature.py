import numpy as np


class GlcmBasedFeature:
    """提取基于灰度共生矩阵的纹理特征"""

    # 灰度共生矩阵
    ret = None
    # 均值
    mean = None
    # 方差
    variance = None

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

    def _angular_second_moment(self):
        """
        计算角二阶矩，图像纹理均一规则时值大
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

    def _entropy(self):
        """
        计算熵，图像纹理复杂时值大
        （灰度共生矩阵值分布均等，即其随机性大）
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

    def _contrast_ratio(self):
        """
        计算对比度，纹理越清晰值越大
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

    def _inverse_differential_moment(self):
        """
        计算反差分矩(逆方差)，纹理清晰规律性强值越大
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

    def _mean(self):
        """
        计算均值，纹理规律性强数值大
        :return: 均值
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        m: np.float = 0.0
        for j in range(height):
            for i in range(width):
                m += self.ret[j][i] * j
        self.mean = m
        return m

    def _variance(self):
        """
        计算方差，图像灰度变化大时数值大
        :return: 方差
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        v: np.float = 0.0
        for j in range(height):
            for i in range(width):
                v += self.ret[j][i] * np.square(j - self.mean)
        self.variance = v
        return v

    def _standard_deviation(self):
        """
        计算标准差，图像灰度变化大时数值大
        :return: 标准差
        """
        std = np.sqrt(self.variance)
        return std

    def _dissimilarity(self):
        """
        计算非相似性，局部对比度搞也会导致数值高
        :return: 非相似性
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        ds: np.float = 0.0
        for j in range(height):
            for i in range(width):
                ds += self.ret[j][i] * np.abs(j - i)
        return ds

    def _correlation(self):
        """
        计算相关性，灰度沿着某方向延伸长则数值高
        :return: 非相似性
        """
        if self.ret is None:
            print("In class 'GlcmBasedFeature': variable 'ret' is None, "
                  "please run method 'glcm()' for calculate glcm first.")
            return
        height, width = self.ret.shape
        cl: np.float = 0.0
        for j in range(height):
            for i in range(width):
                cl += (np.square(self.ret[j][i]) * (j - self.mean) * (i - self.mean)) / self.variance
        return cl

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
        features[0] = self._angular_second_moment()
        features[1] = self._contrast_ratio()
        features[2] = self._entropy()
        features[3] = self._inverse_differential_moment()
        return features
