from PySide2 import QtWidgets
import Qt_Ui.imageWId as iw


class ImageWid(QtWidgets.QWidget, iw.Ui_imageWidget):
    """图片读取和预处理设置窗体的逻辑"""

    def __init__(self):
        super(ImageWid, self).__init__()
        self.setupUi(self)
