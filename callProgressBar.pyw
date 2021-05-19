# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: medical_img_slice_tool
# @File  : callProgressBar.pyw
# @Author: superlee
# @Date  : 2021/5/11

import sys
import threading
import time
from PyQt5.QtWidgets import QDialog, QApplication
from demoProgressBarThread import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class MyThread(threading.Thread):
    counter = 0

    def __init__(self, process_bar):
        threading.Thread.__init__(self)
        self.process_bar = process_bar
        self.counter = 0

    def run(self):
        print("Starting " + self.name)
        while self.counter <= 100:
            time.sleep(1)
            process_bar.ui.progressBar.setValue(self.counter)
            self.counter += 10
            print("Exiting " + self.name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    process_bar = MyForm()
    thread1 = MyThread(process_bar)
    thread1.start()
    process_bar.exec()
    sys.exit(app.exec_())
