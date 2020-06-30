#!/usr/bin/python
#! -*- coding: utf-8 -*-


import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
        command=self.quit)
        self.quitButton.grid()


def main():
    app = Application()
    app.master.title('Sample application')
    app.mainloop()

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))