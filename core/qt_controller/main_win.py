import time

from PySide2.QtCore import Signal, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QMessageBox
from PySide2 import QtWidgets, QtGui
import cv2
import sys

from PySide2.QtGui import QImage
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

from core.qt_controller.path_wid import PathWid
from core.qt_controller.image_wid import ImageWid
from core.qt_controller.feature_fetch_wid import FeatureFetchWid
from core.qt_controller.feature_read_wid import FeatureReadWid
from core.qt_controller.model_wid import ModelWid
from core.qt_controller.predict_wid import PredictWid
from core.qt_controller.predict_result_wid import PredictResultWid

import core.public_signal as public_signal


class MainWin(QtWidgets.QMainWindow, ui_MainWin.Ui_MainWindow):

    def __init__(self, path_wid: PathWid, image_wid: ImageWid, feature_fetch_wid: FeatureFetchWid,
                 feature_read_wid: FeatureReadWid, model_wid: ModelWid, predict_wid: PredictWid,
                 predict_result_wid: PredictResultWid):
        super(MainWin, self).__init__()
        self.setupUi(self)
        # 绑定跳转窗体实例
        self.path_wid = path_wid
        self.image_wid = image_wid
        self.feature_fetch_wid = feature_fetch_wid
        self.feature_read_wid = feature_read_wid
        self.model_wid = model_wid
        self.predict_wid = predict_wid
        self.predict_result_wid = predict_result_wid
        # 创建过程实例
        self.data_set_read = dsr.DataSetRead(ps.PathSome())
        self.data_read = dr.DataRead()
        self.image_read = imr.ImageRead()
        self.image_feature = imf.ImageFeature(True, True, False, False, False, True)
        self.feature_read = fr.FeatureRead()
        self.image_classifier = imc.ImageClassifier(self.feature_read, self.data_set_read)
        # 创建全局信号线程实例
        self.public_signal = public_signal.PublicSignal()
        # 信号槽链接
        self.startButton.clicked.connect(self.start)
        self.dataSetButton.clicked.connect(self.setting_path)
        self.imageButton.clicked.connect(self.setting_image)
        self.featureFetchButton.clicked.connect(self.setting_feature_fetch)
        self.featureReadButton.clicked.connect(self.setting_featrue_read)
        self.modelButton.clicked.connect(self.setting_model)
        self.predictButton.clicked.connect(self.setting_predict)
        # 主流程信号槽连接
        self.dataSetCheckBox.clicked.connect(self.set_feature_fetch_flow)
        self.imageCheckBox.clicked.connect(self.set_feature_fetch_flow)
        self.featureFetchCheckBox.clicked.connect(self.set_feature_fetch_flow)
        self.featureReadCheckBox.clicked.connect(self.set_feature_model_flow)
        self.modelCheckBox.clicked.connect(self.set_feature_model_flow)
        self.predictCheckBox.clicked.connect(self.set_predict_flow)
        # 全局信号实例链接
        self.public_signal.signal_path.connect(self.set_image_path)
        self.public_signal.signal_finish.connect(self.fetch_finished)
        self.public_signal.signal_rewrite.connect(self.file_rewrite)
        self.public_signal.signal_data_set_num.connect(self.set_data_path)
        self.public_signal.signal_feature_read_wid_close(self.set_featrue_read)

    def start(self):
        main_process = mp.MainProcess(self.data_set_read, self.data_read, self.image_read, self.image_feature,
                                      self.feature_read,
                                      self.image_classifier)
        main_process.do_flow(self.featureFetchCheckBox.isChecked(), self.modelCheckBox.isChecked(),
                             self.predictCheckBox.isChecked())

    def setting_path(self):
        self.path_wid.show()

    def setting_image(self):
        self.image_wid.show()

    def setting_feature_fetch(self):
        self.feature_fetch_wid.show()

    def setting_featrue_read(self):
        self.feature_read_wid.show()

    def set_featrue_read(self):
        self.feature_read.set_selection_func(self.feature_read_wid.selection_func)
        self.feature_read.set_k(self.feature_read_wid.k)
        self.feature_read.set_is_normalize(self.feature_read_wid.is_normalize)
        self.feature_read.set_is_regularize(self.feature_read_wid.is_regularize)
        self.feature_read.set_is_transform(self.feature_read_wid.is_transform)

    def setting_model(self):
        self.model_wid.show()

    def setting_predict(self):
        self.predict_wid.show()

    def show_predict_result(self, data):
        self.predict_result_wid.set_result_data(data)
        self.predict_result_wid.show()

    def set_data_path(self, data_set_num: int):
        self.data_set_read.data_set_num = data_set_num

    def set_image_path(self, image_path: str):
        self.infoLabel.setText(str(image_path))
        self.imageLabel.setPixmap(QPixmap(image_path).scaled(self.imageLabel.height(), self.imageLabel.height()))
        QApplication.processEvents()

    def fetch_finished(self):
        reply = QMessageBox.information(self,
                                        "提示消息",
                                        "特征提取完成！已保存在对应文件中。",
                                        QMessageBox.Yes)
        print(reply)

    def file_rewrite(self):
        reply = QMessageBox.information(self,
                                        "提示消息",
                                        "特征文件已存在，是否覆写？",
                                        QMessageBox.Yes | QMessageBox.No)
        if str(reply).split('.')[4] == 'Yes':
            self.public_signal.send_rewrite_choose('y')
        else:
            self.public_signal.send_rewrite_choose('n')

    def set_feature_fetch_flow(self):
        if self.dataSetCheckBox.checkState() == Qt.Checked or self.imageCheckBox.checkState() == Qt.Checked or self.featureFetchCheckBox.checkState() == Qt.Checked:
            self.dataSetCheckBox.setCheckState(Qt.Checked)
            self.imageCheckBox.setCheckState(Qt.Checked)
            self.featureFetchCheckBox.setCheckState(Qt.Checked)
            self.featureReadCheckBox.setCheckState(Qt.Unchecked)
            self.modelCheckBox.setCheckState(Qt.Unchecked)
            self.predictCheckBox.setCheckState(Qt.Unchecked)

    def set_feature_model_flow(self):
        if self.modelCheckBox.checkState() == Qt.Checked or self.featureReadCheckBox.checkState() == Qt.Checked:
            self.featureReadCheckBox.setCheckState(Qt.Checked)
            self.modelCheckBox.setCheckState(Qt.Checked)
            self.dataSetCheckBox.setCheckState(Qt.Unchecked)
            self.imageCheckBox.setCheckState(Qt.Unchecked)
            self.featureFetchCheckBox.setCheckState(Qt.Unchecked)
            self.predictCheckBox.setCheckState(Qt.Unchecked)

    def set_predict_flow(self):
        if self.predictCheckBox.checkState() == Qt.Checked:
            self.imageCheckBox.setCheckState(Qt.Unchecked)
            self.featureFetchCheckBox.setCheckState(Qt.Unchecked)
            self.featureReadCheckBox.setCheckState(Qt.Unchecked)
            self.modelCheckBox.setCheckState(Qt.Unchecked)
