# todo: 这个文件要处理读取图片和标签的问题
import glob


class DataSetRead:
    """处理各数据集的读取"""

    def read_image(self, data_set_num: int):
        if data_set_num == 0:
            self.img_path = self.standard_set_dict['data']
        elif data_set_num == 1:
            self.img_path = glob.glob(self.data_set_1 + '/' + '*' + '/*/*' + 'jpg')
        elif data_set_num == 2:
            self.img_path = glob.glob(self.data_set_2 + '/' + '*' + '/*/*' + 'png')
        else:
            pass
