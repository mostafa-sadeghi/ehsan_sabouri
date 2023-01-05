import tkinter as tk

from tkinter import ttk, END

numbers = []
operators = []


def button_equal():
    statement = e.get()
    e.delete(0, END)
    for index, s in enumerate(statement):
        if s == "+":
            operators.append(s)
            numbers.append(statement[:index])
            numbers.append(statement[index+1:])

    print(numbers)


def button_add():
    e.insert(END, "+")


def button_clear():
    e.delete(0, END)


def button_click(number):
    e.insert(END, number)


def button_subtract():
    e.insert(END, "-")


def button_multiply():
    e.insert(END, "×")


def button_division():
    e.insert(END, "÷")


root = tk.Tk()
root.columnconfigure(0, weight=1)
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TButton", bordercolor="silver", width=2,
                borderwidth=2, relief="solid", font=15, background="lightblue", padding=(1, 1))
style.configure("TEntry", bordercolor="black", padding=(25, 5), fieldbackground="lightblue",
                borderwidth=5, relief="solid", font=15)
style.configure("TFrame", bordercolor="green", relief="solid")
print(style.layout("TFrame"))
print(style.element_options("Frame.border"))
# print(style.lookup("TButton", "font"))

root.title('calculator')

e = ttk.Entry(root, width=15)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

frame = ttk.Frame(root, padding=(25, 5))
frame.grid(row=1, column=0)
# add buttons
button_1 = ttk.Button(frame, text="1",
                      command=lambda: button_click(1))
button_2 = ttk.Button(frame, text="2",
                      command=lambda: button_click(2))
button_3 = ttk.Button(frame, text="3",
                      command=lambda: button_click(3))
button_4 = ttk.Button(frame, text="4",
                      command=lambda: button_click(4))
button_5 = ttk.Button(frame, text="5",
                      command=lambda: button_click(5))
button_6 = ttk.Button(frame, text="6",
                      command=lambda: button_click(6))
button_7 = ttk.Button(frame, text="7",
                      command=lambda: button_click(7))
button_8 = ttk.Button(frame, text="8",
                      command=lambda: button_click(8))
button_9 = ttk.Button(frame, text="9",
                      command=lambda: button_click(9))
button_0 = ttk.Button(frame, text="0",
                      command=lambda: button_click(0))
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)


button_add = ttk.Button(frame, text="+", command=button_add)
button_equal = ttk.Button(frame, text="=", command=button_equal)
button_clear = ttk.Button(frame, text="clear", command=button_clear)

button_clear.grid(row=4, column=1, columnspan=2, sticky="ew")
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2, sticky="ew")

button_sub = ttk.Button(frame, text="-", command=button_subtract)
button_mul = ttk.Button(frame, text="×", command=button_multiply)
button_div = ttk.Button(frame, text="÷", command=button_division)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)


# end button widgets
root.mainloop()
