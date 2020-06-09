"""
@File : path_wid.py
@Time : 2020/06/09 16:27:49
@Author : Jyunmau
@Version : 1.0
"""

from PySide2 import QtWidgets
import Qt_Ui.pathWid as pw
import core.public_signal as ps
import core.path_some as pts


class PathWid(QtWidgets.QWidget, pw.Ui_pathWidget):
    """数据集路径设置窗体的逻辑"""

    def __init__(self):
        super(PathWid, self).__init__()
        self.setupUi(self)
        self.path_some = pts.PathSome()
        self.pathLabel.setText(self.path_some.data_set_2)
        self.ds0RadioButton.clicked.connect(self.set_path_label)
        self.ds1RadioButton.clicked.connect(self.set_path_label)
        self.ds2RadioButton.clicked.connect(self.set_path_label)

    def set_path_label(self):
        if self.ds0RadioButton.isChecked():
            self.pathLabel.setText(self.path_some.data_set_standard)
        elif self.ds1RadioButton.isChecked():
            self.pathLabel.setText(self.path_some.data_set_1)
        elif self.ds2RadioButton.isChecked():
            self.pathLabel.setText(self.path_some.data_set_2)

    def closeEvent(self, event):
        cls = ps.PublicSignal()
        data_set_num = 2
        if self.ds0RadioButton.isChecked():
            data_set_num = 0
        elif self.ds1RadioButton.isChecked():
            data_set_num = 1
        elif self.ds2RadioButton.isChecked():
            data_set_num = 2
        cls.send_data_set_num(data_set_num)
