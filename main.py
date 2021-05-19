# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: pyqt5_learn
# @File  : main
# @Author: super
# @Date  : 2021/5/18
import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

"""
    GUI
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())