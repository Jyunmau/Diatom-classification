# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jyunmau/PycharmProjects/Diatom-classification/Qt_Ui/pathWid.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_pathWidget(object):
    def setupUi(self, pathWidget):
        pathWidget.setObjectName("pathWidget")
        pathWidget.resize(500, 350)
        self.verticalLayoutWidget = QtWidgets.QWidget(pathWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 481, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pathLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pathLabel.setObjectName("pathLabel")
        self.verticalLayout.addWidget(self.pathLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ds0RadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ds0RadioButton.setObjectName("ds0RadioButton")
        self.horizontalLayout.addWidget(self.ds0RadioButton)
        self.ds0PushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ds0PushButton.setObjectName("ds0PushButton")
        self.horizontalLayout.addWidget(self.ds0PushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ds1RadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ds1RadioButton.setObjectName("ds1RadioButton")
        self.horizontalLayout_2.addWidget(self.ds1RadioButton)
        self.ds1PushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ds1PushButton.setObjectName("ds1PushButton")
        self.horizontalLayout_2.addWidget(self.ds1PushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ds2RadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ds2RadioButton.setChecked(True)
        self.ds2RadioButton.setObjectName("ds2RadioButton")
        self.horizontalLayout_3.addWidget(self.ds2RadioButton)
        self.ds2PushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ds2PushButton.setObjectName("ds2PushButton")
        self.horizontalLayout_3.addWidget(self.ds2PushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(pathWidget)
        QtCore.QMetaObject.connectSlotsByName(pathWidget)

    def retranslateUi(self, pathWidget):
        _translate = QtCore.QCoreApplication.translate
        pathWidget.setWindowTitle(_translate("pathWidget", "图片数据集路径设置"))
        self.pathLabel.setText(_translate("pathWidget", "等待设置路径..."))
        self.ds0RadioButton.setText(_translate("pathWidget", "数据集0: cifar-10"))
        self.ds0PushButton.setText(_translate("pathWidget", "更改路径"))
        self.ds1RadioButton.setText(_translate("pathWidget", "数据集1: 179张，12类"))
        self.ds1PushButton.setText(_translate("pathWidget", "更改路径"))
        self.ds2RadioButton.setText(_translate("pathWidget", "数据集2: 296张，9类"))
        self.ds2PushButton.setText(_translate("pathWidget", "更改路径"))
