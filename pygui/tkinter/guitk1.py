# -*- coding: utf-8 -*- 

from Tkinter import *

class LabelDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Label Demo")
        self.grid()
        self._label = Label(self, text="Hello World!")
        self._label.grid()
        
def main():
    demo = LabelDemo()
    demo.mainloop()

if __name__ == "__main__":
    main()