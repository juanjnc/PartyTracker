import tkinter as tk
from tkinter import messagebox as mb
from os import startfile


class Raiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Initiative Tracker'), self.geometry('600x660'), self.iconbitmap('ico.ico')


class Tracker(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.btn_0 = tk.Button(self, text="Add", fg='green', command=self.linea, font=('Arial', 10), cursor='hand2', bd=3)
        self.btn_0.grid(column=0, row=0)
        self.btn_1 = tk.Button(self, text="Delete Last", fg='red', command=None, font=('Arial', 10), cursor='hand2', bd=3)
        self.btn_1.grid(column=1, row=0)
        self.label = tk.Label(self, text='-----------------------------------', font=('Arial', 10))
        self.label.grid(column=0, row=1, columnspan=2)
        self.grid(sticky='n')

    def linea(self):

        def erase():
            init_label.destroy(), init.destroy(), name_label.destroy(), name.destroy(), hp_label.destroy(), hp.destroy()
            ac_label.destroy(), ac.destroy(), clean_btn.destroy()

        def clean():
            init.delete(0, 1000), name.delete(0, 1000), hp.delete(0, 1000), ac.delete(0, 1000)

        self.btn_1.configure(command=erase)
        init_label = tk.Label(self, text='Initiative/Round Order', font=('Arial', 10), fg='red')
        init_label.grid(columnspan=2)
        init = tk.Entry(self, font=('Arial', 10), justify='center', fg='red4')
        init.grid(columnspan=2)
        name_label = tk.Label(self, text='Name', font=('Arial', 10), fg='blue')
        name_label.grid(columnspan=2)
        name = tk.Entry(self, font=('Arial', 10), justify='center', fg='blue4')
        name.grid(columnspan=2)
        hp_label = tk.Label(self, text='Hit/Life Points', font=('Arial', 10), justify='center', fg='green')
        hp_label.grid(columnspan=2)
        hp = tk.Entry(self, font=('Arial', 10), justify='center')
        hp.grid(columnspan=2)
        ac_label = tk.Label(self, text='AC/Armor/Defense', font=('Arial', 10))
        ac_label.grid(columnspan=2)
        ac = tk.Entry(self, font=('Arial', 10), justify='center')
        ac.grid(columnspan=2)
        clean_btn = tk.Button(self, text='Clean Entry', command=clean, font=('Arial', 10), cursor='hand2', bd=2, fg='yellow4')
        clean_btn.grid(columnspan=2)


class Menus(tk.Menu):  # Gestiona la barra de menú
    def __init__(self, container):
        super().__init__(container)
        archivo_menu = tk.Menu(self, tearoff=0)
        archivo_menu.add_command(label='Exit', command=self.exit)
        self.add_cascade(label='File', menu=archivo_menu,)
        ayuda_menu = tk.Menu(self, tearoff=0)
        ayuda_menu.add_command(label='Version', command=self.version)
        ayuda_menu.add_command(label='Changelog', command=self.changes)
        ayuda_menu.add_command(label='About...', command=self.info)
        self.add_cascade(label='Help', menu=ayuda_menu)
        root.config(menu=self)

    @staticmethod
    def info():
        mb.showinfo('Info Initiative Tracker', 'Programmed in Python by Juan José Núñez.\n(https://www.python.org/)'
                                               '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)')

    @staticmethod
    def version():
        mb.showinfo('Version', 'Initiative Tracker 1.2.2')

    @staticmethod
    def changes():
        startfile('changelog.txt')

    @staticmethod
    def exit():
        valor = mb.askokcancel('Close', 'Are you sure?')
        if valor is True:
            root.destroy()


if __name__ == "__main__":
    root = Raiz()
    menu = Menus(root)
    # Add a canvas in that frame
    # canvas = tk.Canvas(root)
    # canvas.grid(row=0, column=0, sticky="news")
    # Link a scrollbar to the canvas
    # vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    # vsb.grid(row=0, column=1, sticky='ns')
    # canvas.configure(yscrollcommand=vsb.set)
    # canvas.config(scrollregion=canvas.bbox("all"))
    app0 = Tracker(root)
    app0.grid(column=0, row=0)
    app1 = Tracker(root)
    app1.grid(column=1, row=0)
    app2 = Tracker(root)
    app2.grid(column=2, row=0)
    app3 = Tracker(root)
    app3.grid(column=3, row=0)
    root.mainloop()
