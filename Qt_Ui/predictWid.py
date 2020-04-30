# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jyunmau/PycharmProjects/Diatom-classification/Qt_Ui/predictWid.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_predictWidget(object):
    def setupUi(self, predictWidget):
        predictWidget.setObjectName("predictWidget")
        predictWidget.resize(500, 350)
        self.verticalLayoutWidget = QtWidgets.QWidget(predictWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 481, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wrongOnlyCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.wrongOnlyCheckBox.setBaseSize(QtCore.QSize(0, 0))
        self.wrongOnlyCheckBox.setAutoFillBackground(False)
        self.wrongOnlyCheckBox.setTristate(False)
        self.wrongOnlyCheckBox.setObjectName("wrongOnlyCheckBox")
        self.horizontalLayout.addWidget(self.wrongOnlyCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.modelLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.modelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modelLabel.setObjectName("modelLabel")
        self.verticalLayout_2.addWidget(self.modelLabel)
        self.modelPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.modelPushButton.setObjectName("modelPushButton")
        self.verticalLayout_2.addWidget(self.modelPushButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dataLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dataLabel.setObjectName("dataLabel")
        self.verticalLayout_3.addWidget(self.dataLabel)
        self.dataPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dataPushButton.setObjectName("dataPushButton")
        self.verticalLayout_3.addWidget(self.dataPushButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(predictWidget)
        QtCore.QMetaObject.connectSlotsByName(predictWidget)

    def retranslateUi(self, predictWidget):
        _translate = QtCore.QCoreApplication.translate
        predictWidget.setWindowTitle(_translate("predictWidget", "预测设置"))
        self.wrongOnlyCheckBox.setText(_translate("predictWidget", "只展示错分图片"))
        self.modelLabel.setText(_translate("predictWidget", "等待设置模型路径..."))
        self.modelPushButton.setText(_translate("predictWidget", "设置模型路径"))
        self.dataLabel.setText(_translate("predictWidget", "等待设置数据路径..."))
        self.dataPushButton.setText(_translate("predictWidget", "设置数据路径"))
