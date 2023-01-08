from tkinter import ttk
import tkinter as tk


def handle_scale(event):
    print(scale.get())


root = tk.Tk()

scale = ttk.Scale(root, orient="horizontal", from_=0,
                  to=10, command=handle_scale)
scale.pack()

root.mainloop()
