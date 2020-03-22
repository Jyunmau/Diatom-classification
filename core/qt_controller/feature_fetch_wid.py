from PySide2 import QtWidgets
import Qt_Ui.featureFetchWid as ffw


class FeatureFetchWid(QtWidgets.QWidget, ffw.Ui_featureFetchWidget):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self):
        super(FeatureFetchWid, self).__init__()
        self.setupUi(self)
