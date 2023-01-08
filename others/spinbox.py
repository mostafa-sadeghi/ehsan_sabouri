from tkinter import ttk
import tkinter as tk
root = tk.Tk()
initial_val = tk.IntVar(value=20)
spin_box = ttk.Spinbox(root, from_=0, to=30,
                       textvariable=initial_val, wrap=True)
spin_box.pack()
root.mainloop()
