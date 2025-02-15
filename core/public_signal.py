# -*- coding:utf-8 -*-
"""
@File : public_signal.py
@Time : 2020/06/09 16:22:38
@Author : Jyunmau
@Version : 1.0
"""

import glob
import os
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal
from PySide2.QtCore import QThread, Signal

import core.qt_controller.main_win as mw


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class PublicSignal(QThread):
    """
    用于主逻辑与QT_UI交互的信号槽，单例
    """
    signal_path = Signal(str)
    signal_finish = Signal()
    signal_rewrite = Signal()
    signal_rewrite_choose = Signal(str)
    signal_data_set_num = Signal(int)
    signal_feature_read_wid_close = Signal()
    signal_predict_result = Signal(str, str, str)
    signal_predict_next = Signal()
    signal_feature_code_fetch = Signal(bool, bool, bool, bool, bool, bool)
    signal_feature_code_read = Signal(bool, bool, bool, bool, bool, bool)

    def send_image_path(self, image_path: str):
        self.signal_path.emit(image_path)

    def send_finished(self):
        self.signal_finish.emit()

    def send_rewrite(self):
        self.signal_rewrite.emit()

    def send_rewrite_choose(self, choose: str):
        self.signal_rewrite_choose.emit(choose)

    def send_data_set_num(self, data_set_num: int):
        self.signal_data_set_num.emit(data_set_num)

    def send_signal_feature_read_wid_close(self):
        self.signal_feature_read_wid_close.emit()

    def send_signal_predict_result(self, real_label: str, predict_label: str, image_path: str):
        self.signal_predict_result.emit(real_label, predict_label, image_path)

    def send_signal_predict_next(self):
        self.signal_predict_next.emit()

    def send_feature_code_fetch(self, geo: bool, glcm: bool, fd: bool, hog: bool, sift: bool, lbp: bool):
        self.signal_feature_code_fetch.emit(geo, glcm, fd, hog, sift, lbp)

    def send_feature_code_read(self, geo: bool, glcm: bool, fd: bool, hog: bool, sift: bool, lbp: bool):
        self.signal_feature_code_read.emit(geo, glcm, fd, hog, sift, lbp)
