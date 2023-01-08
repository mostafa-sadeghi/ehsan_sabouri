# list boxes:
from tkinter import ttk
import tkinter as tk


def handle_selection(event):
    selected_indices = list_box.curselection()
    for i in selected_indices:
        print(list_box.get(i))


root = tk.Tk()
programming_languages = ("c", "c++", "java", "python")
langs = tk.StringVar(value=programming_languages)

list_box = tk.Listbox(root, listvariable=langs,
                      height=6, selectmode="extended")
list_box.bind("<<ListboxSelect>>", handle_selection)
list_box.pack()
root.mainloop()
