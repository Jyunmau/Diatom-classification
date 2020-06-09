# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jyunmau/PycharmProjects/Diatom-classification/Qt_Ui/predictResultWid.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_predictResltWid(object):
    def setupUi(self, predictResltWid):
        predictResltWid.setObjectName("predictResltWid")
        predictResltWid.resize(500, 350)
        self.horizontalLayoutWidget = QtWidgets.QWidget(predictResltWid)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.imageLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
        self.lastPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.lastPushButton.setObjectName("lastPushButton")
        self.verticalLayout.addWidget(self.lastPushButton)
        self.nextPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextPushButton.setObjectName("nextPushButton")
        self.verticalLayout.addWidget(self.nextPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.predictLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.predictLabel.setText("")
        self.predictLabel.setObjectName("predictLabel")
        self.horizontalLayout_3.addWidget(self.predictLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.realLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.realLabel.setText("")
        self.realLabel.setObjectName("realLabel")
        self.horizontalLayout_2.addWidget(self.realLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(predictResltWid)
        QtCore.QMetaObject.connectSlotsByName(predictResltWid)

    def retranslateUi(self, predictResltWid):
        _translate = QtCore.QCoreApplication.translate
        predictResltWid.setWindowTitle(_translate("predictResltWid", "图片预测"))
        self.infoLabel.setText(_translate("predictResltWid", "TextLabel"))
        self.imageLabel.setText(_translate("predictResltWid", "等待加载图片..."))
        self.lastPushButton.setText(_translate("predictResltWid", "上一张"))
        self.nextPushButton.setText(_translate("predictResltWid", "下一张"))
        self.label.setText(_translate("predictResltWid", "预测类别："))
        self.label_3.setText(_translate("predictResltWid", "真实类别："))
