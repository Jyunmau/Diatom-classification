"""
@File : predict_result_wid.py
@Time : 2020/06/09 16:30:49
@Author : Jyunmau
@Version : 1.0
"""

from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication

import Qt_Ui.predictResultWid as prw
import core.public_signal as ps


class PredictResultWid(QtWidgets.QWidget, prw.Ui_predictResltWid):
    """识别结果弹窗的窗体逻辑"""

    data = None

    def __init__(self):
        super(PredictResultWid, self).__init__()
        self.setupUi(self)
        self.public_signal = ps.PublicSignal()
        self.public_signal.signal_predict_result.connect(self.set_result_data)
        self.nextPushButton.clicked.connect(self.predict_next)

    def set_result_data(self, real, predict, img_path):
        self.infoLabel.setText(img_path)
        self.imageLabel.setPixmap(QPixmap(img_path).scaled(self.imageLabel.height(), self.imageLabel.height()))
        QApplication.processEvents()
        # self.imageLabel.setText(img)
        self.predictLabel.setText(predict)
        self.realLabel.setText(real)

    def predict_next(self):
        print('push_next')
        self.public_signal.send_signal_predict_next()
