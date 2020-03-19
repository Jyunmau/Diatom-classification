import time

from PySide2 import QtWidgets
import sys

from PySide2.QtWidgets import QApplication

import Qt_Ui.MainWin as ui_MainWin
import core.main_process as mp
import core.path_some as ps
import core.data_preprocessing.data_set_read as dsr
import core.data_preprocessing.data_read as dr
import core.image_processing.image_read as imr
import core.feature_processing.image_feature as imf
import core.data_preprocessing.feature_read as fr
import core.classifier.image_classifier as imc

import core.public_signal as public_signal


class MainWin(QtWidgets.QMainWindow, ui_MainWin.Ui_MainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        # 创建过程实例
        self.data_set_read = dsr.DataSetRead(ps.PathSome())
        self.data_read = dr.DataRead(self.data_set_read)
        self.image_read = imr.ImageRead()
        self.image_feature = imf.ImageFeature(True, True, False, False, False, True)
        self.feature_read = fr.FeatureRead()
        self.image_classifier = imc.ImageClassifier(self.feature_read)
        # 信号槽链接
        self.startButton.clicked.connect(self.start)
        # 全局信号实例链接
        self.image_feature.signal_path.connect(self.set_image_path)

    def start(self):
        main_process = mp.MainProcess(self.data_read, self.image_read, self.image_feature, self.feature_read,
                                      self.image_classifier)
        main_process.do_flow()

    def set_image_path(self, image_path: str):
        print(self.infoLabel.text())
        self.infoLabel.setText(str(image_path))
        QApplication.processEvents()
