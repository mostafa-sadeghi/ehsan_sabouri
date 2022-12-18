from tkinter import ttk
import tkinter as tk
import tkinter.font as font


class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container)
        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="nothing")
        metres_label = ttk.Label(self, text='Metres:')
        metres_input = ttk.Entry(
            self, width=10, textvariable=self.metres_value, font=("Times New Roman", 15))
        feet_label = ttk.Label(self, text='Feet:')
        feet_display = ttk.Label(self, text="Feet shown here:",
                                 textvariable=self.feet_value)
        calc_button = ttk.Button(
            self, text="calculate", command=self.calculate)

        switch_page_button = ttk.Button(self, text="switch to feet to metres",
                                        command=lambda: controller.show_frame(FeetToMetres))

        metres_label.grid(column=0, row=0, sticky='w')
        metres_input.grid(column=1, row=0, sticky='ew')
        metres_input.focus()
        feet_label.grid(column=0, row=1, sticky='w')
        feet_display.grid(column=1, row=1, sticky='ew')
        calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        metres = float(self.metres_value.get())
        feet = metres * 3.2
        self.feet_value.set(f'{feet:.3f}')
        # print(f'{metres} metres is equal to {feet:.3f} feet')


class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container)
        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar(value="nothing")
        feet_label = ttk.Label(self, text='Feet:')
        feet_input = ttk.Entry(
            self, width=10, textvariable=self.feet_value, font=("Times New Roman", 15))
        metres_label = ttk.Label(self, text='Metres:')
        metres_display = ttk.Label(self, text="Feet shown here:",
                                   textvariable=self.metres_value)
        calc_button = ttk.Button(
            self, text="calculate", command=self.calculate)

        switch_page_button = ttk.Button(
            self, text="switch to metres to feet", command=lambda: controller.show_frame(MetresToFeet))

        feet_label.grid(column=0, row=0, sticky='w')
        feet_input.grid(column=1, row=0, sticky='ew')
        feet_input.focus()
        metres_label.grid(column=0, row=1, sticky='w')
        metres_display.grid(column=1, row=1, sticky='ew')
        calc_button.grid(column=0, row=2, columnspan=2, sticky='ew')
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        feet = float(self.feet_value.get())
        metres = feet / 3.2
        self.metres_value.set(f'{metres:.3f}')
        # print(f'{metres} metres is equal to {feet:.3f} feet')


class DistanceConvertor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Distance Convertor")
        self.frames = dict()
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky='ew')
        feet_to_metres = FeetToMetres(container, self, padding=(60, 30))
        feet_to_metres.grid(row=0, column=0, sticky='ewns')

        metres_to_feet = MetresToFeet(container, self)
        metres_to_feet.grid(row=0, column=0, sticky='ewns')
        # feet_to_metres.tkraise()

        self.frames[FeetToMetres] = feet_to_metres
        self.frames[MetresToFeet] = metres_to_feet

        self.show_frame(MetresToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        self.bind("<Return>", frame.calculate)


root = DistanceConvertor()
font.nametofont("TkDefaultFont").configure(family="Times New Roman", size=15)
root.columnconfigure(0, weight=1)
root.title('Distance convertor')


root.mainloop()
