import sys

from PyQt5 import QtWidgets

from core.qt_controller.main_win import MainWin


# from Core.ResultWid import ResultWid
# from Core.ImageRecognition import ImageRecognition
# from Core.SingleResultWid import SingleResultWid


def main():
    app = QtWidgets.QApplication(sys.argv)
    # image_recognition = ImageRecognition()
    # result_wid = ResultWid(image_recognition)
    # single_result_wid = SingleResultWid(image_recognition)
    main_win = MainWin()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
