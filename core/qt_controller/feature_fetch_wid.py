"""
@File : feature_fetch_wid.py
@Time : 2020/06/09 16:29:49
@Author : Jyunmau
@Version : 1.0
"""

from PySide2 import QtWidgets
import Qt_Ui.featureFetchWid as ffw
import core.public_signal as public_signal


class FeatureFetchWid(QtWidgets.QWidget, ffw.Ui_featureFetchWidget):
    """特征提取参数设置的窗体逻辑"""

    def __init__(self):
        super(FeatureFetchWid, self).__init__()
        self.setupUi(self)
        # 创建全局信号线程实例
        self.public_signal = public_signal.PublicSignal()
        # self.yesButton.clicked.connect(self.chg_feature_code)

    def closeEvent(self, event):
        self.public_signal.send_feature_code_fetch(self.geometricCheckBox.isChecked(), self.glcmCheckBox.isChecked(),
                                                   self.fdCheckBox.isChecked(), self.hogCheckBox.isChecked(),
                                                   self.siftCheckBox.isChecked(), self.lbpCheckBox.isChecked())
