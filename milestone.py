from tkinter import ttk
import tkinter as tk
import tkinter.font as font


class MetresToFeet(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="nothing")
        metres_label = ttk.Label(root.frame, text='Metres:')
        metres_input = ttk.Entry(
            root.frame, width=10, textvariable=metres_value, font=("Times New Roman", 15))
        feet_label = ttk.Label(root.frame, text='Feet:')
        feet_display = ttk.Label(root.frame, text="Feet shown here:",
                                 textvariable=feet_value)
        calc_button = ttk.Button(
            root.frame, text="calculate", command=calculate_feet)

        metres_label.grid(column=0, row=0, sticky='w')
        metres_input.grid(column=1, row=0, sticky='ew')
        metres_input.focus()
        feet_label.grid(column=0, row=1, sticky='w')
        feet_display.grid(column=1, row=1, sticky='ew')
        calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')


for child in root.frame.winfo_children():
    child.grid_configure(padx=15, pady=15)

    def calculate_feet(self, *args):
        metres = float(self.metres_value.get())
        feet = metres * 3.2
        self.feet_value.set(f'{feet:.3f}')
        # print(f'{metres} metres is equal to {feet:.3f} feet')


class DistanceConvertor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Distance Convertor")
        self.frame = ttk.Frame(self, padding=(60, 30))
        self.frame.grid()


root = DistanceConvertor()
font.nametofont("TkDefaultFont").configure(family="Times New Roman", size=15)
root.columnconfigure(0, weight=1)
root.title('Distance convertor')


metres_input.bind("<Return>", calculate_feet)
root.mainloop()
