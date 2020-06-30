# -*- coding: utf-8 -*-

from Tkinter import *


class ImageDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Python Powered")
        self.grid()
        self._image = PhotoImage(file="python-512.gif")
        self._image_label = Label(self, image=self._image)
        self._image_label.grid()
        self._text_label = Label(self, text="Python Powered !!")
        self._text_label.grid()

def main():
    image_demo = ImageDemo()
    image_demo.mainloop()

if __name__ == "__main__":
    main()