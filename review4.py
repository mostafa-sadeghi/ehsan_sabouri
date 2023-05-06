import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

style.configure('custom.TButton', font=("Arial", 18, "bold"),
                foreground="blue", width=9, padding=10, border=5, relief="raised")

ttk.Label(root, text="Username", anchor="nw",
          background="orange", underline=1, foreground="blue", width=9, font=("Arial", 18, "bold"), justify="center", borderwidth=5, relief="raised", padding=10, cursor="hand2").pack(side="left")
my_button = ttk.Button(root, text="Submit")
my_button.pack(side="left")
my_button = ttk.Button(root, text="Submit", style="custom.TButton")
my_button.pack(side="left")
# print(my_button.winfo_class())

root.mainloop()
