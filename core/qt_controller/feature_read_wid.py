from PySide2 import QtWidgets
import Qt_Ui.featureReadWid as frw


class FeatureReadWid(QtWidgets.QWidget, frw.Ui_featureReadWidget):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self):
        super(FeatureReadWid, self).__init__()
        self.setupUi(self)
