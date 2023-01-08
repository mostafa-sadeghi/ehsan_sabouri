import tkinter as tk
from tkinter import ttk


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sample")
        ttk.Label(self, text='sample').pack()


root = HelloWorld()
frame = UserInputFrame(root)
frame.pack()
root.mainloop()
