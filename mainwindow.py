# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: pyqt5_learn
# @File  : mainwindow
# @Author: super
# @Date  : 2021/5/18

import time
from PyQt5.QtWidgets import QMainWindow
from ui_mainwindow import *
from threads import WorkThread

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 绑定点击事件
        self.button_ok.clicked.connect(self.button_start)

    def button_start(self):
        # 设置按钮不可用
        self.button_ok.setChecked(True)
        self.button_ok.setDisabled(True)
        # 创建子线程处理逻辑事务
        self.th = WorkThread(ip='192.168.1.1', port=4000)
        # 绑定子线程的th的信号finishSignal和Ui主线程中的槽函数button_finish
        self.th.finishSignal.connect(self.button_finish)
        # 启动线程
        self.th.start()
        # time.sleep(20)

    def button_finish(self, msg):
        print('msg: {}'.format(msg))
        # 设置按钮可用
        self.button_ok.setChecked(False)
        self.button_ok.setDisabled(False)