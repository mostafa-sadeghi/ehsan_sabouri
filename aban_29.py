import tkinter as tk
from tkinter import ttk
root = tk.Tk()


# ttk.Label(root, text="hello ", padding=20).pack()
# ttk.Separator(root, orient="horizontal").pack(fill="x")
# ttk.Label(root, text="hello ", padding=20).pack()

check_button = ttk.Checkbutton(root, text="ckeck me!")
check_button.pack()
check_button['state'] = 'disabled'
selected_option = tk.StringVar()


def print_current():
    print(selected_option.get())


check_button = ttk.Checkbutton(root, text="ckeck me!", variable=selected_option,
                               command=print_current, onvalue="ok", offvalue="not ok")
check_button.pack()

ttk.Label(root, textvariable=selected_option).pack()

storage_variable = tk.StringVar()


style = ttk.Style(root)
style.configure("TRadiobutton", background="light blue")


# def print_current():
#     print(storage_variable.get())


# # radio button
option_one = ttk.Radiobutton(
    root, text="option 1", variable=storage_variable, value="first option", command=print_current)
option_two = ttk.Radiobutton(
    root, text="option 2", variable=storage_variable, value="second option", command=print_current)
option_three = ttk.Radiobutton(
    root, text="option 3", variable=storage_variable, value="third option", command=print_current)
option_one.pack()
option_two.pack()
option_three.pack()

select_weekday = tk.StringVar()


# def handle_selection(event):
#     print("seleted value is: ", select_weekday.get())


# weekday = ttk.Combobox(root, textvariable=select_weekday)
# weekday["values"] = ("Mon", "Tue", "thur")
# weekday["state"] = "readonly"
# weekday.current(0)
# weekday.bind("<<ComboboxSelected>>", handle_selection)

# weekday.pack()


root.mainloop()
