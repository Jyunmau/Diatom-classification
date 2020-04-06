from PySide2 import QtWidgets
import Qt_Ui.featureReadWid as frw


class FeatureReadWid(QtWidgets.QWidget, frw.Ui_featureReadWidget):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self):
        super(FeatureReadWid, self).__init__()
        self.setupUi(self)
        self.k = self.featureNumSpinBox.text()
        self.selection_func = self.featureSelectionComboBox.currentText()
        self.is_regularize = self.regularizeCheckBox.isChecked()
        self.is_normalize = self.normalizeCheckBox.isChecked()
        self.is_transform = self.transformCheckBox.isChecked()

    def closeEvent(self, event):
        self.k = self.featureNumSpinBox.text()
        self.selection_func = self.featureSelectionComboBox.currentText()
        self.is_regularize = self.regularizeCheckBox.isChecked()
        self.is_normalize = self.normalizeCheckBox.isChecked()
        self.is_transform = self.transformCheckBox.isChecked()
