"""
@File : main.py
@Time : 2020/06/09 16:25:00
@Author : Jyunmau
@Version : 1.0
"""

import sys

from PyQt5 import QtWidgets

from core.qt_controller.main_win import MainWin

# from Core.ResultWid import ResultWid
# from Core.ImageRecognition import ImageRecognition
# from Core.SingleResultWid import SingleResultWid

from core.qt_controller.path_wid import PathWid
from core.qt_controller.image_wid import ImageWid
from core.qt_controller.feature_fetch_wid import FeatureFetchWid
from core.qt_controller.feature_read_wid import FeatureReadWid
from core.qt_controller.model_wid import ModelWid
from core.qt_controller.predict_wid import PredictWid
from core.qt_controller.predict_result_wid import PredictResultWid


def main():
    """
    QT窗体程序的主入口文件
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    # image_recognition = ImageRecognition()
    # result_wid = ResultWid(image_recognition)
    # single_result_wid = SingleResultWid(image_recognition)
    path_wid = PathWid()
    image_wid = ImageWid()
    feature_fetch_wid = FeatureFetchWid()
    feature_read_wid = FeatureReadWid()
    model_wid = ModelWid()
    predict_wid = PredictWid()
    predict_result_wid = PredictResultWid()
    main_win = MainWin(path_wid, image_wid, feature_fetch_wid, feature_read_wid, model_wid, predict_wid,
                       predict_result_wid)
    main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
