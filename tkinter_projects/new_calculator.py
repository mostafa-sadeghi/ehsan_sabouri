# about eval function
# x = '1+2*3/2'
# z = eval(x)
# print(z)


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Calculator')
root.iconbitmap('./tkinter_projects/favicon.ico')
root.geometry('320x450')

# style
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TEntry", bordercolor="cyan",
                lightcolor="black", fieldbackground="lightblue", padding=(45, 20))
style.configure("TButton", bordercolor="cyan", font=('Arial', 20, 'normal'), padding=12, width=5,
                lightcolor="black", fieldbackground="lightblue", background="lightblue")

print(style.layout('TButton'))
print(style.element_options("Button.label"))


entry_box = ttk.Entry(root, width=15, font=('Arial', 20, 'bold'))
entry_box.grid(row=0, column=0, columnspan=3)

# adding buttons
button_7 = ttk.Button(root, text='7')
button_7.grid(row=1, column=0)
button_8 = ttk.Button(root, text='8')
button_8.grid(row=1, column=1)
button_9 = ttk.Button(root, text='9')
button_9.grid(row=1, column=2)

button_4 = ttk.Button(root, text='4')
button_4.grid(row=2, column=0)
button_5 = ttk.Button(root, text='5')
button_5.grid(row=2, column=1)
button_6 = ttk.Button(root, text='6')
button_6.grid(row=2, column=2)

button_1 = ttk.Button(root, text='1')
button_1.grid(row=3, column=0)
button_2 = ttk.Button(root, text='2')
button_2.grid(row=3, column=1)
button_3 = ttk.Button(root, text='3')
button_3.grid(row=3, column=2)

button_point = ttk.Button(root, text='.')
button_point.grid(row=4, column=0)
button_open_p = ttk.Button(root, text='(')
button_open_p.grid(row=4, column=1)
button_close_p = ttk.Button(root, text=')')
button_close_p.grid(row=4, column=2)

button_add = ttk.Button(root, text='+')
button_add.grid(row=5, column=0)
button_sub = ttk.Button(root, text='-')
button_sub.grid(row=5, column=1)
button_mul = ttk.Button(root, text='×')
button_mul.grid(row=5, column=2)

button_div = ttk.Button(root, text='÷')
button_div.grid(row=6, column=0)
button_clear = ttk.Button(root, text='c')
button_clear.grid(row=6, column=1)
button_equql = ttk.Button(root, text='=')
button_equql.grid(row=6, column=2)


root.mainloop()
