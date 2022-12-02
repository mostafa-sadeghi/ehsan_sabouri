from tkinter import ttk
import tkinter as tk
import tkinter.font as font

root = tk.Tk()
font.nametofont("TkDefaultFont").configure(family="Times New Roman", size=15)
root.columnconfigure(0, weight=1)
root.title('Distance convertor')
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="nothing")


def calculate_feet(*args):
    metres = float(metres_value.get())
    feet = metres * 3.2
    feet_value.set(f'{feet:.3f}')
    # print(f'{metres} metres is equal to {feet:.3f} feet')


main = ttk.Frame(root, padding=(30, 15))
main.grid()
metres_label = ttk.Label(main, text='Metres:')
metres_input = ttk.Entry(
    main, width=10, textvariable=metres_value, font=("Times New Roman", 15))
feet_label = ttk.Label(main, text='Feet:')
feet_display = ttk.Label(main, text="Feet shown here:",
                         textvariable=feet_value)
calc_button = ttk.Button(main, text="calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, sticky='w')
metres_input.grid(column=1, row=0, sticky='ew')
metres_input.focus()
feet_label.grid(column=0, row=1, sticky='w')
feet_display.grid(column=1, row=1, sticky='ew')
calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

metres_input.bind("<Return>", calculate_feet)
root.mainloop()
