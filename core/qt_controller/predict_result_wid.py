from PySide2 import QtWidgets
import Qt_Ui.predictResultWid as prw
import core.public_signal as ps


class PredictResultWid(QtWidgets.QWidget, prw.Ui_predictResltWid):
    """单张图片识别结果的窗体逻辑"""

    data = None

    def __init__(self):
        super(PredictResultWid, self).__init__()
        self.setupUi(self)
        self.public_signal = ps.PublicSignal()

    def set_result_data(self, data):
        self.data = data
