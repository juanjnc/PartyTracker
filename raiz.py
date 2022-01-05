from tkinter import *


class Raiz(Tk):
    def __init__(self):
        super().__init__()
        self.title('Initiative Tracker v2')
        self.geometry('690x740')
        img = PhotoImage(file=r'ico.png')
        self.wm_iconphoto(True, img)
