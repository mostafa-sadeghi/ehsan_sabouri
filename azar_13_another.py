import tkinter as tk
from tkinter import ttk


class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "sample"
        ttk.Label(self, text='sample').pack()


root = HelloWorld()
root.mainloop()
