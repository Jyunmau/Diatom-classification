# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jyunmau/PycharmProjects/Diatom-classification/Qt_Ui/imageWId.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_imageWidget(object):
    def setupUi(self, imageWidget):
        imageWidget.setObjectName("imageWidget")
        imageWidget.resize(500, 350)
        self.verticalLayoutWidget = QtWidgets.QWidget(imageWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fIlterCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fIlterCheckBox.setChecked(True)
        self.fIlterCheckBox.setObjectName("fIlterCheckBox")
        self.horizontalLayout.addWidget(self.fIlterCheckBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.filterComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterComboBox.sizePolicy().hasHeightForWidth())
        self.filterComboBox.setSizePolicy(sizePolicy)
        self.filterComboBox.setEditable(False)
        self.filterComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.filterComboBox.setDuplicatesEnabled(False)
        self.filterComboBox.setObjectName("filterComboBox")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.verticalLayout_4.addWidget(self.filterComboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.filterSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterSpinBox.sizePolicy().hasHeightForWidth())
        self.filterSpinBox.setSizePolicy(sizePolicy)
        self.filterSpinBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.filterSpinBox.setFont(font)
        self.filterSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.filterSpinBox.setMinimum(3)
        self.filterSpinBox.setMaximum(7)
        self.filterSpinBox.setSingleStep(2)
        self.filterSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.filterSpinBox.setProperty("value", 3)
        self.filterSpinBox.setObjectName("filterSpinBox")
        self.verticalLayout_3.addWidget(self.filterSpinBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(imageWidget)
        self.filterComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(imageWidget)

    def retranslateUi(self, imageWidget):
        _translate = QtCore.QCoreApplication.translate
        imageWidget.setWindowTitle(_translate("imageWidget", "图片预处理设置"))
        self.fIlterCheckBox.setText(_translate("imageWidget", "平滑滤波"))
        self.label_2.setText(_translate("imageWidget", "卷积核类型："))
        self.filterComboBox.setCurrentText(_translate("imageWidget", "高斯核"))
        self.filterComboBox.setItemText(0, _translate("imageWidget", "高斯核"))
        self.filterComboBox.setItemText(1, _translate("imageWidget", "中值"))
        self.label.setText(_translate("imageWidget", "卷积核大小："))
