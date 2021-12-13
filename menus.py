from tkinter import *
import menusFunctions as mf


class Menus(Menu):  # Gestiona la barra de menú
    def __init__(self, container, **kwargs):
        super().__init__(container)
        archivo_menu = Menu(self, tearoff=0)
        archivo_menu.add_command(label='Exit', command=mf.create_cerrar_method(**kwargs))
        self.add_cascade(label='File', menu=archivo_menu)
        ayuda_menu = Menu(self, tearoff=0)
        ayuda_menu.add_command(label='Version', command=mf.version)
        ayuda_menu.add_command(label='Changelog', command=mf.changes)
        ayuda_menu.add_command(label='License', command=mf.mitlicense)
        ayuda_menu.add_command(label='About...', command=mf.info)
        self.add_cascade(label='Help', menu=ayuda_menu)
        container.config(menu=self)
