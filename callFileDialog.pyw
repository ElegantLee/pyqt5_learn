# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: medical_img_slice_tool
# @File  : demoFileDiaolog
# @Author: superlee
# @Date  : 2021/5/9

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from demoQFileDialog import *


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.openFileDialog)
        self.ui.actionSave.triggered.connect(self.saveFileDialog)
        self.show()

    def openFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', 'D:/')
        if fname[0]:
            f = open(fname[0], 'r')
        with f:
            data = f.read()
            self.ui.textEdit.setText(data)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        f = open(fileName, 'w')
        text = self.ui.textEdit.toPlainText()
        f.write(text)
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
