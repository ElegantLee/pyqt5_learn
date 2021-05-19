# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: pyqt5_learn
# @File  : threads
# @Author: super
# @Date  : 2021/5/18

import time
from PyQt5.QtCore import QThread, pyqtSignal


class WorkThread(QThread):
    finishSignal = pyqtSignal(str)

    def __init__(self, ip, port, parent=None):
        super(WorkThread, self).__init__(parent)
        self.ip = ip
        self.port = port

    def run(self):
        print('===================sleep==================ip: {}, port: {}'.format(self.ip, self.port))
        time.sleep(20)

        self.finishSignal.emit('This is a test.')
        return
