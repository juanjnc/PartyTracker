from tkinter import *
from tkinter import messagebox as mb
from os import startfile


class Menus(Menu):  # Gestiona la barra de menú
    def __init__(self, container, **kwargs):
        super().__init__(container)
        archivo_menu = Menu(self, tearoff=0)
        archivo_menu.add_command(label='Exit', command=self.create_cerrar_method(**kwargs))
        self.add_cascade(label='File', menu=archivo_menu)
        ayuda_menu = Menu(self, tearoff=0)
        ayuda_menu.add_command(label='Version', command=self.version)
        ayuda_menu.add_command(label='Changelog', command=self.changes)
        ayuda_menu.add_command(label='About...', command=self.info)
        self.add_cascade(label='Help', menu=ayuda_menu)
        container.config(menu=self)

    @staticmethod
    def info():
        mb.showinfo('Info Initiative Tracker', 'Programmed in Python by Juan José Núñez.\n(https://www.python.org/)'
                                               '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)')

    @staticmethod
    def version():
        mb.showinfo('Version', 'Initiative Tracker 2.0.0')

    @staticmethod
    def changes():
        startfile('changelog.txt')

    @staticmethod
    def create_cerrar_method(root):
        def cerrar():
            valor = mb.askokcancel('Close', 'Are you sure?')
            if valor is True: root.destroy()
        return cerrar
