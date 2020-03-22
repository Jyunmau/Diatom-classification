# -*- coding:utf-8 -*-
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
    signal_path = Signal(str)
    signal_finish = Signal()
    signal_rewrite = Signal()
    signal_rewrite_choose = Signal(str)
    signal_data_set_num = Signal(int)

    def send_image_path(self, image_path: str):
        self.signal_path.emit(image_path)

    def send_finished(self):
        self.signal_finish.emit()

    def send_rewrite(self):
        self.signal_rewrite.emit()

    def send_rewrite_choose(self, choose: str):
        self.signal_rewrite_choose.emit(choose)

    def send_data_set_num(self, data_set_num: int):
        self.signal_data_set_num(data_set_num)
