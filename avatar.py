from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="avatar!").grid(column=1, row=2)
ttk.Button(frm, text="exit", command=root.destroy).grid(column=0, row=0)
root.mainloop()