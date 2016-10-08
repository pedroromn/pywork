# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:28:55 2016

@author: peyo
"""

import sys
# from PySide.QtCore import *
from PySide.QtGui import QMainWindow, QApplication


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("First GUI")


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
