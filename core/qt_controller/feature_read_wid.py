"""
@File : feature_read_wid.py
@Time : 2020/06/09 16:29:26
@Author : Jyunmau
@Version : 1.0
"""

from PySide2 import QtWidgets
import Qt_Ui.featureReadWid as frw
import core.public_signal as public_signal


class FeatureReadWid(QtWidgets.QWidget, frw.Ui_featureReadWidget):
    """特征读取参数设置的窗体逻辑"""

    def __init__(self):
        super(FeatureReadWid, self).__init__()
        self.setupUi(self)
        self.k = self.featureNumSpinBox.text()
        self.selection_func = self.featureSelectionComboBox.currentText()
        self.is_regularize = self.regularizeCheckBox.isChecked()
        self.is_normalize = self.normalizeCheckBox.isChecked()
        self.is_transform = self.transformCheckBox.isChecked()
        self.public_signal = public_signal.PublicSignal()

    def closeEvent(self, event):
        self.k = self.featureNumSpinBox.text()
        self.selection_func = self.featureSelectionComboBox.currentText()
        self.is_regularize = self.regularizeCheckBox.isChecked()
        self.is_normalize = self.normalizeCheckBox.isChecked()
        self.is_transform = self.transformCheckBox.isChecked()
        self.public_signal.send_feature_code_read(self.geometricCheckBox.isChecked(), self.glcmCheckBox.isChecked(),
                                                  self.fdCheckBox.isChecked(), self.hogCheckBox.isChecked(),
                                                  self.siftCheckBox.isChecked(), self.lbpCheckBox.isChecked())
