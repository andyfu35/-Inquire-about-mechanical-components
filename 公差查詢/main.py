from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.pyplot import text
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pandas as pd
import sys
import os
import TEST as ui


PATH = "公差查詢/參數/"
data_name = os.listdir(PATH)
class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.comboBox.addItems(data_name)
         self.comboBox.currentTextChanged.connect(self.box_1)
         self.comboBox_2.currentTextChanged.connect(self.box_2)
         self.comboBox_3.currentTextChanged.connect(self.box_3)
         self.textList = [self.label_4,self.label_5,self.label_6,self.label_7,self.label_8,self.label_9,self.label_10,self.label_11,self.label_12,self.label_13,self.label_14,self.label_15,self.label_16,self.label_17,self.label_18,self.label_19,self.label_20]
    def box_1(self):
        text_1 = self.comboBox.currentText()
        type_path_1 = PATH + text_1 + "/"
        type_name_1 = os.listdir(type_path_1)
        type_name_2 = []
        for T in range(len(type_name_1)):
            type_name_2.append(type_name_1[T].replace(".csv", ""))
        self.comboBox_2.clear()
        self.comboBox_2.addItems(type_name_2)
    def box_2(self):
        # self.label_4.setText(_translate("Form", "種類"))
        text_1 = self.comboBox.currentText()
        text_2 = self.comboBox_2.currentText()
        type_path_2 = PATH + text_1 + "/" + text_2 + ".csv"
        dataframe = pd.read_csv(type_path_2, sep=",")
        index = dataframe.values[0, 0]
        dataframe = pd.read_csv(type_path_2, sep=",", index_col=index)
        self.comboBox_3.clear()
        for i in dataframe.index:
            self.comboBox_3.addItem(str(i))
    def box_3(self):
        _translate = QtCore.QCoreApplication.translate
        text_1 = self.comboBox.currentText()
        text_2 = self.comboBox_2.currentText()
        text_3 = self.comboBox_3.currentText()
        type_path_2 = PATH + text_1 + "/" + text_2 + ".csv"
        dataframe = pd.read_csv(type_path_2, sep=",")
        index = dataframe.values[0, 0]
        dataframe = pd.read_csv(type_path_2, sep=",", index_col=index)
        columns = dataframe.columns.values

        for i in range(len(columns)):
            self.textList[i].setText(_translate("Form", columns[i]))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())