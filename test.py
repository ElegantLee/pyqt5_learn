# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: demoProgressBarThread.ui
# @File  : test
# @Author: superlee
# @Date  : 2021/4/26

from ui.medical_img_slice_tool import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class ExitDesignerGUI():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.widget_actions()
        sys.exit(app.exec_())

    def widget_actions(self):
        self.ui.actionexit.setStatusTip('点击关闭程序')
        self.ui.actionexit.triggered.connect(self.close_GUI)

    def close_GUI(self):
        self.MainWindow.close()

    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')


if __name__ == "__main__":
    ExitDesignerGUI()

