from PySide2 import QtWidgets
import Qt_Ui.featureFetchWid as ffw
import core.public_signal as public_signal


class FeatureFetchWid(QtWidgets.QWidget, ffw.Ui_featureFetchWidget):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self):
        super(FeatureFetchWid, self).__init__()
        self.setupUi(self)
        # 创建全局信号线程实例
        self.public_signal = public_signal.PublicSignal()
        self.yesButton.clicked.connect(self.chg_feature_code)

    def chg_feature_code(self):
        self.public_signal.send_feature_code(self.geometricCheckBox.isChecked(), self.glcmCheckBox.isChecked(),
                                             self.fdCheckBox.isChecked(), self.hogCheckBox.isChecked(),
                                             self.siftCheckBox.isChecked(), self.lbpCheckBox.isChecked())
