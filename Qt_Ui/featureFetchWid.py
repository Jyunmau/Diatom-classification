# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jyunmau/PycharmProjects/Diatom-classification/Qt_Ui/featureFetchWid.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_featureFetchWidget(object):
    def setupUi(self, featureFetchWidget):
        featureFetchWidget.setObjectName("featureFetchWidget")
        featureFetchWidget.resize(500, 350)
        self.verticalLayoutWidget = QtWidgets.QWidget(featureFetchWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.geometricCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geometricCheckBox.sizePolicy().hasHeightForWidth())
        self.geometricCheckBox.setSizePolicy(sizePolicy)
        self.geometricCheckBox.setChecked(True)
        self.geometricCheckBox.setAutoExclusive(False)
        self.geometricCheckBox.setObjectName("geometricCheckBox")
        self.horizontalLayout_6.addWidget(self.geometricCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.glcmCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.glcmCheckBox.setChecked(True)
        self.glcmCheckBox.setObjectName("glcmCheckBox")
        self.horizontalLayout_5.addWidget(self.glcmCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fdCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fdCheckBox.setObjectName("fdCheckBox")
        self.horizontalLayout_4.addWidget(self.fdCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hogCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.hogCheckBox.setObjectName("hogCheckBox")
        self.horizontalLayout_3.addWidget(self.hogCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.siftCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.siftCheckBox.setObjectName("siftCheckBox")
        self.horizontalLayout.addWidget(self.siftCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbpCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.lbpCheckBox.setChecked(True)
        self.lbpCheckBox.setObjectName("lbpCheckBox")
        self.horizontalLayout_2.addWidget(self.lbpCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.yesButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.yesButton.setObjectName("yesButton")
        self.verticalLayout.addWidget(self.yesButton)

        self.retranslateUi(featureFetchWidget)
        QtCore.QMetaObject.connectSlotsByName(featureFetchWidget)

    def retranslateUi(self, featureFetchWidget):
        _translate = QtCore.QCoreApplication.translate
        featureFetchWidget.setWindowTitle(_translate("featureFetchWidget", "特征提取设置"))
        self.geometricCheckBox.setText(_translate("featureFetchWidget", "基于统计和几何的形状特征"))
        self.glcmCheckBox.setText(_translate("featureFetchWidget", "基于灰度共生矩阵的纹理特征"))
        self.fdCheckBox.setText(_translate("featureFetchWidget", "傅立叶描述子特征"))
        self.hogCheckBox.setText(_translate("featureFetchWidget", "HOG算子特征"))
        self.siftCheckBox.setText(_translate("featureFetchWidget", "SIFT算子特征"))
        self.lbpCheckBox.setText(_translate("featureFetchWidget", "LBP算子特征"))
        self.yesButton.setText(_translate("featureFetchWidget", "确定"))
