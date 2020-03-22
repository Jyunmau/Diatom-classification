from PySide2 import QtWidgets
import Qt_Ui.modelWid as mw


class ModelWid(QtWidgets.QWidget, mw.Ui_modelWIdget):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self):
        super(ModelWid, self).__init__()
        self.setupUi(self)
