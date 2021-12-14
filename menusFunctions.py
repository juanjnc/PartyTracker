from tkinter import messagebox as mb
from os import startfile


def version():
    mb.showinfo('Version', 'Initiative Tracker 2.0.1')


def info():
    mb.showinfo('Info Initiative Tracker', 'Copyright (c) 2021 Juan José Núñez Cózar under MIT License'
                                           '\nWebsite: https://github.com/shurkun-juan/PartyTracker'
                                           '\n\nProgrammed in Python.\n(https://www.python.org/)'
                                           '\n\nIcons made by Ana Canalejo.\n(https://www.deviantart.com/miyuminineko)'
                                           '\n\nThanks to Rubén, Steph and Mauro for the help and support provided.')


def mitlicense(): return mb.showinfo('License', 'MIT License'
                                                '\n\nCopyright (c) 2021 Juan José Núñez Cózar'
                                                '\n\nPermission is hereby granted, free of charge, to any person '
                                                'obtaining a copy of this software and associated documentation files '
                                                '(the "Software"), to deal in the Software without restriction, '
                                                'including without limitation the rights to use, copy, modify, merge, '
                                                'publish, distribute, sublicense, and/or sell copies of the Software, '
                                                'and to permit persons to whom the Software is furnished to do so, '
                                                'subject to the following conditions: '
                                                '\n\nThe above copyright notice and this permission notice shall be '
                                                'included in all copies or substantial portions of the Software.'
                                                '\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, '
                                                'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF '
                                                'MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND '
                                                'NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS '
                                                'BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN '
                                                'ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN '
                                                'CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE '
                                                'SOFTWARE.')


def changes():
    startfile('changelog.txt')


def create_cerrar_method(root):
    def cerrar():
        valor = mb.askokcancel('Close', 'Are you sure?')
        if valor is True: root.destroy()

    return cerrar
