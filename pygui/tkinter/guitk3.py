# -*- coding : utf-8 -*- 

from Tkinter import Frame
from Tkinter import Label
from Tkinter import Button


class ButtonDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Button Demo")
        self.grid()
        self._label = Label(self, text="Hello")
        self._label.grid()
        self._button = Button(self,
                              text="Click me",
                              command=self._switch)
        self._button.grid()

    def _switch(self):
        if self._label["text"] == "Hello":
            self._label["text"] == "Goodbye"
        else:
            self._label["text"] == "Hello"


def main():
    demo = ButtonDemo()
    demo.mainloop()


if __name__ == "__main__":
    main()
