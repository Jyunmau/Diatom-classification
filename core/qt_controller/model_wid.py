"""
@File : model_wid.py
@Time : 2020/06/09 16:27:39
@Author : Jyunmau
@Version : 1.0
"""

from PySide2 import QtWidgets
import Qt_Ui.modelWid as mw


class ModelWid(QtWidgets.QWidget, mw.Ui_modelWIdget):
    """模型训练的窗体逻辑"""

    def __init__(self):
        super(ModelWid, self).__init__()
        self.setupUi(self)
