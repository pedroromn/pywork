# -*- coding: utf-8 -*-


import sys
from PySide import QtCore, QtGui


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.create_gui()

    def create_gui(self):
        quit = QtGui.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        lcd = QtGui.QLCDNumber(2)

        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)

        self.connect(quit, QtCore.SIGNAL("clicked()"),
                     QtGui.qApp, QtCore.SLOT("quit()"))
        self.connect(slider, QtCore.SIGNAL("valueChanged(int)"),
                     lcd, QtCore.SLOT("display(int)"))

        layout = QtGui.QVBoxLayout()
        layout.addWidget(quit)
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


def main():
    app = QtGui.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
