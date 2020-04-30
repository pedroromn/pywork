#! -*- coding: utf-8 -*-
# labeltk.py
# Label demonstration


from Tkinter import *

class LabelDemo(Frame):

    def __init__(self):
        Frame.__init__(self) # initializes Frame object

        # frame fills all available space
        self.pack( expand = YES, fill = BOTH )
        self.master.title("Labels")

        self.label1 = Label(self, text="Label with text")

        # resize frame to accomodate Label
        self.label1.pack()

        self.label2 = Label(self, text="Labels with text and bitmap")

        self.label2.pack( side = LEFT )

        # using default bitmap image as label
        self.label3 = Label(self, bitmap="warning")
        self.label3.pack( side = LEFT )

