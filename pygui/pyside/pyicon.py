# -*- coding: utf-8 -*-
"""
Created on Fri May 13 21:07:37 2016

@author: peyo
"""

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.__init_view()
        
    def __init_view(self):
        QtGui.QToolTip.setFont(QtGui.QFont("SansSerif", 10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QtGui.QPushButton("Quit", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.move(50, 50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        

def main():
    app = QtGui.QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
