# about eval function
# x = '1+2*3/2'
# z = eval(x)
# print(z)


import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def show(value):
    global entry_val
    entry_val += value
    equation.set(entry_val)


def solve():
    result = eval(entry_val)
    equation.set(result)


def clear():
    global entry_val
    entry_val = ''
    equation.set(entry_val)


max_len = 15


def on_write(*args):
    s = equation.get()
    if len(s) > max_len:
        equation.set(s[:max_len])


root = tk.Tk()
root.title('Calculator')
root.iconbitmap('./tkinter_projects/favicon.ico')
root.geometry('273x400')
root.resizable(False, False)

entry_val = ''
equation = tk.StringVar()

# style
style = ttk.Style('darkly')
# style.theme_use('clam')
style.configure("TEntry", bordercolor="cyan",
                lightcolor="black", fieldbackground="lightblue")
style.configure("TButton", bordercolor="cyan", font=('Arial', 20, 'bold'), width=4,
                lightcolor="black", fieldbackground="lightblue", background="lightblue")


entry_box = ttk.Entry(root, width=15, font=(
    'Arial', 20, 'bold'), textvariable=equation, bootstyle="secondary")
entry_box.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(1, 10))

equation.trace_variable("w", on_write)


# adding buttons
button_7 = ttk.Button(
    root, text='7', command=lambda: show('7'), bootstyle="success, outline",)
button_7.grid(row=1, column=0, padx=(0, 10), pady=(0, 10),)
button_8 = ttk.Button(
    root, text='8', command=lambda: show('8'), bootstyle="success, outline")
button_8.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))
button_9 = ttk.Button(
    root, text='9', command=lambda: show('9'), bootstyle="success, outline")
button_9.grid(row=1, column=2, padx=(0, 10), pady=(0, 10))

button_4 = ttk.Button(
    root, text='4', command=lambda: show('4'), bootstyle="success, outline")
button_4.grid(row=2, column=0, padx=(0, 10), pady=(0, 10))
button_5 = ttk.Button(
    root, text='5', command=lambda: show('5'), bootstyle="success, outline")
button_5.grid(row=2, column=1, padx=(0, 10), pady=(0, 10))
button_6 = ttk.Button(
    root, text='6', command=lambda: show('6'), bootstyle="success, outline")
button_6.grid(row=2, column=2, padx=(0, 10), pady=(0, 10))

button_1 = ttk.Button(
    root, text='1', command=lambda: show('1'), bootstyle="success, outline")
button_1.grid(row=3, column=0, padx=(0, 10), pady=(0, 10))
button_2 = ttk.Button(
    root, text='2', command=lambda: show('2'), bootstyle="success, outline")
button_2.grid(row=3, column=1, padx=(0, 10), pady=(0, 10))
button_3 = ttk.Button(
    root, text='3', command=lambda: show('3'), bootstyle="success, outline")
button_3.grid(row=3, column=2, padx=(0, 10), pady=(0, 10))

button_point = ttk.Button(
    root, text='.', command=lambda: show('.'), bootstyle="primary, outline")
button_point.grid(row=4, column=0, padx=(0, 10), pady=(0, 10))
button_open_p = ttk.Button(
    root, text='(', command=lambda: show('('), bootstyle="primary, outline")
button_open_p.grid(row=4, column=1, padx=(0, 10), pady=(0, 10))
button_close_p = ttk.Button(root, text=')',
                            command=lambda: show(')'), bootstyle="primary, outline")
button_close_p.grid(row=4, column=2, padx=(0, 10), pady=(0, 10))

button_add = ttk.Button(
    root, text='+', command=lambda: show('+'), bootstyle="danger, outline")
button_add.grid(row=5, column=0, padx=(0, 10), pady=(0, 10))
button_sub = ttk.Button(
    root, text='-', command=lambda: show('-'), bootstyle="danger, outline")
button_sub.grid(row=5, column=1, padx=(0, 10), pady=(0, 10))
button_mul = ttk.Button(
    root, text='×', command=lambda: show('*'), bootstyle="danger, outline")
button_mul.grid(row=5, column=2, padx=(0, 10), pady=(0, 10))

button_div = ttk.Button(
    root, text='÷', command=lambda: show('/'), bootstyle="danger, outline")
button_div.grid(row=6, column=0, padx=(0, 10), pady=(0, 10))
button_clear = ttk.Button(root, text='c', command=clear,
                          bootstyle="danger")
button_clear.grid(row=6, column=1, padx=(0, 10), pady=(0, 10))
button_equql = ttk.Button(root, text='=', command=solve, bootstyle="danger")
button_equql.grid(row=6, column=2, padx=(0, 10), pady=(0, 10))


root.mainloop()
