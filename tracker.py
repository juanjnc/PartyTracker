from tkinter import *
from tkinter.ttk import *


class Tracker(Frame):
    def __init__(self, container):
        super().__init__(container)
        Style().configure('T1.TButton', font=('Arial', 10), cursor='hand2', borderwidth=3, foreground='green')
        Style().configure('T2.TButton', font=('Arial', 10), cursor='hand2', borderwidth=3, foreground='red')
        Style().configure('T.TLabel', font=('Arial', 10))
        self.btn_0 = Button(self, text="Add", command=self.linea, style='T1.TButton', width=10)
        self.btn_0.grid(column=0, row=0)
        self.btn_1 = Button(self, text="Delete Last", command=None, style='T2.TButton', width=10)
        self.btn_1.grid(column=1, row=0)
        self.label = Label(self, text='-----------------------------------', style='T.TLabel')
        self.label.grid(column=0, row=1, columnspan=2)
        self.grid(sticky='n')

    def linea(self):

        def erase():
            init_label.destroy(), init.destroy(), name_label.destroy(), name.destroy(), hp_label.destroy(), hp.destroy()
            ac_label.destroy(), ac.destroy(), clean_btn.destroy()

        def clean():
            init.delete(0, 1000), name.delete(0, 1000), hp.delete(0, 1000), ac.delete(0, 1000)

        Style().configure('E1.TEntry', font=('Arial', 10))
        Style().configure('C.TLabel', font=('Arial', 10))
        Style().configure('C.TButton', font=('Arial', 10), cursor='hand2', bd=3, foreground='yellow4', borderwidth=2)
        self.btn_1.configure(command=erase)
        init_label = Label(self, text='Initiative/Round Order', font=('Arial', 10), foreground='red')
        init_label.grid(columnspan=2)
        init = Entry(self, style='E1.TEntry', justify='center', foreground='red4')
        init.grid(columnspan=2)
        name_label = Label(self, text='Name', style='C.TLabel', foreground='blue')
        name_label.grid(columnspan=2)
        name = Entry(self, style='E1.TEntry', justify='center', foreground='blue4')
        name.grid(columnspan=2)
        hp_label = Label(self, text='Hit/Life Points', style='C.TLabel', justify='center', foreground='green')
        hp_label.grid(columnspan=2)
        hp = Entry(self, style='E1.TEntry', justify='center')
        hp.grid(columnspan=2)
        ac_label = Label(self, text='AC/Armor/Defense', style='C.TLabel')
        ac_label.grid(columnspan=2)
        ac = Entry(self, style='E1.TEntry', justify='center')
        ac.grid(columnspan=2)
        clean_btn = Button(self, text='Clean Entry', command=clean,  style='C.TButton')
        clean_btn.grid(columnspan=2)
