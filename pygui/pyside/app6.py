#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import sys
from PySide import QtCore, QtGui


class LCDRange(QtGui.QWidget):
    """ LCDRange con slider  """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._create_components()

    def _create_components(self):
        lcd = QtGui.QLCDNumber(2)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)
        self.connect(slider, QtCore.SIGNAL("valueChanged(int)"),
                     lcd, QtCore.SLOT("display(int)"))

        layout = QtGui.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)
