# -*- coding:utf-8 -*-
import glob
import os
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal
import core.qt_controller.main_win as mw


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class PublicSignal(QObject):
    image_path: str
    image: np.array
    signal_1 = pyqtSignal(str)

    def set_image_path(self, image_path: str):
        self.image_path = image_path
        self.signal_1.emit(image_path)
