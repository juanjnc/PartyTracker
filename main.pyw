from raiz import Raiz
from menus import Menus
from tracker import Tracker

if __name__ == "__main__":
    root = Raiz()
    dict_agr = dict(root=root)
    menu = Menus(root, **dict_agr)
    app0 = Tracker(root)
    app0.grid(column=0, row=0)
    app1 = Tracker(root)
    app1.grid(column=1, row=0)
    app2 = Tracker(root)
    app2.grid(column=2, row=0)
    app3 = Tracker(root)
    app3.grid(column=3, row=0)
    root.mainloop()
