# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: medical_img_slice_tool
# @File  : callProgressBarTwoThreads
# @Author: superlee
# @Date  : 2021/5/11

import sys
import threading
import time
from PyQt5.QtWidgets import QDialog, QApplication
from demoTwoProgressBars import *


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class MyThread(threading.Thread):
    counter = 0

    def __init__(self, w, ProgressBar):
        super(MyThread, self).__init__()
        self.w = w
        self.counter = 0
        self.progressBar = ProgressBar

    def run(self):
        print("Starting " + self.name + "n")
        while self.counter <= 100:
            time.sleep(1)
            self.progressBar.setValue(self.counter)
            self.counter += 10
            print("Exiting " + self.name + "n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    thread1 = MyThread(w, w.ui.progressBarFileDownload)
    thread2 = MyThread(w, w.ui.progressBarVirusScan)
    thread1.start()
    thread2.start()
    w.exec()
    thread1.join()
    thread2.join()
    sys.exit(app.exec_())

