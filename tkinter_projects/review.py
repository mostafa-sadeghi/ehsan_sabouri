# GUI
# Web
# Database

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from image_converter import convert_image


def open_file_dialog():
    path = filedialog.askopenfilename()
    convert_image(path, image_mode, file_name.get())


def handle_selection(event):
    # print(format_images.current())
    global image_mode
    image_mode = format_images.get()


root = tk.Tk()
root.geometry("400x320")
root.title("برنامه من")
root.iconbitmap("apple.ico")

image_formats = tk.StringVar()
image_mode = ''
file_name = tk.StringVar()
ttk.Entry(root, textvariable=file_name).pack(pady=(5, 10))


format_images = ttk.Combobox(root, textvariable=image_formats)
format_images.pack(pady=(0, 10))
format_images["values"] = ("JPEG", "PNG")
format_images.bind("<<ComboboxSelected>>", handle_selection)
ttk.Button(root, text="open", command=open_file_dialog,
           cursor="hand2", padding=10).pack()


root.mainloop()
