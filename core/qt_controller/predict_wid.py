"""
@File : predict_wid.py
@Time : 2020/06/09 16:28:12
@Author : Jyunmau
@Version : 1.0
"""

from PySide2 import QtWidgets
import Qt_Ui.predictWid as pw


class PredictWid(QtWidgets.QWidget, pw.Ui_predictWidget):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self):
        super(PredictWid, self).__init__()
        self.setupUi(self)
