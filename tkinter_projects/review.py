# GUI
# Web
# Database

import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from tkinter import filedialog
from image_converter import convert_image


def open_file_dialog():
    path = filedialog.askopenfilename()
    convert_image(path, image_mode, file_name.get())


def handle_selection(event):
    # print(format_images.current())
    global image_mode
    image_mode = format_images.get()


# root = tk.Tk()


# style = ttk.Style()
root = ttk.Window(themename="superhero")
# style.configure('TButton', font=("Arial", 16))
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# style.theme_use('xpnative')
# print(style.theme_names())
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("400x220")
root.title("برنامه من")
root.iconbitmap("apple.ico")

image_formats = tk.StringVar()
image_mode = ''
file_name = tk.StringVar()


header_frame = ttk.Frame(root)
header_frame.grid(row=0, column=0)
header_frame.columnconfigure(0, weight=1)
header_frame.columnconfigure(1, weight=1)
header_frame.rowconfigure(0, weight=1)
ttk.Label(header_frame, text="File name:", padding=10, anchor="w", justify="left",
          font=("Arial", 16)).grid(row=0, column=0)
ttk.Entry(header_frame, textvariable=file_name,
          font=("Arial", 16)).grid(row=0, column=1)


body_frame = ttk.Frame(root)
body_frame.grid(row=1, column=0)
body_frame.columnconfigure(0, weight=1)
body_frame.columnconfigure(1, weight=1)
body_frame.rowconfigure(0, weight=1)
ttk.Label(body_frame, text="Image Format:", padding=(0, 0, 70, 0), anchor="w",
          font=("Arial", 16)).grid(row=0, column=0, sticky="w")
format_images = ttk.Combobox(
    body_frame, textvariable=image_formats, font=("Arial", 16), width=10)
format_images.grid(row=0, column=1)
format_images["values"] = ("JPEG", "PNG")
format_images.bind("<<ComboboxSelected>>", handle_selection)
ttk.Button(body_frame, text="open", command=open_file_dialog,
           cursor="hand2", padding=20).grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)


root.mainloop()
