import tkinter as tk
from tkinter import ttk


def greet(*args):
    print(f'Hello,{user_name.get()}')


root = tk.Tk()
style = ttk.Style(root)

# print(style.theme_names())
# print(style.theme_use())
style.theme_use('clam')
style.configure("CustomEntryStyle.TEntry", padding=20)
style.configure("Emergency.CustomEntryStyle.TEntry", padding=10)
style.configure("TLabel", font=("Arial", 20))
style.configure("TLabel", bordercolor="#f00")
style.configure("TLabel", borderwidth=10)
style.configure("TLabel", relief="solid")
# print(style.layout("TLabel"))
# print(style.element_options("Label.border"))
# print(style.element_options("Label.padding"))
# print(style.element_options("Label.label"))
# print(style.lookup("TLabel", "font"))
# print(style.lookup("TLabel", "foreground"))
main = ttk.Frame(root, padding=(140, 20))
main.grid()
user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name: ", style="TLabel")
name_label["style"] = "TLabel"
name_label.grid(row=0, column=0, padx=(0, 10))

# print(name_label.winfo_class())

name_entry = ttk.Entry(main, width=16, textvariable=user_name)
name_entry["style"] = "CustomEntryStyle.TEntry"
name_entry.grid(row=0, column=1, padx=10)

# print(name_entry.winfo_class())
name_entry.focus()
greet_button = ttk.Button(main, text='Greet', command=greet)
greet_button.grid(row=0, column=2, sticky='ew', padx=10)
root.mainloop()
