import tkinter as tk
from tkinter import ttk
from collections import deque


class PomodoroTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pomodoro timer')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        container = ttk.Frame(self)
        container.columnconfigure(0, weight=1)

        container.grid(row=0, column=0)
        timer_frame = Timer(container)
        timer_frame.grid(row=0, column=0, sticky="NEWS")


class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.current_time = tk.StringVar(value="00:10")
        self.timer_order = ["Pomodoro", "Short Break",
                            "Pomodoro", "Short Break",
                            "pomodoro", "long Break"]
        self.timer_schedule = deque(self.timer_order)

        self.current_timer_label = tk.StringVar(value=self.timer_schedule[0])

        self.timer_running = True

        timer_description = ttk.Label(
            self, textvariable=self.current_timer_label)
        timer_description.grid(row=0, column=0, sticky="w")

        timer_frame = ttk.Frame(self)
        timer_frame.grid(sticky="NSEW")

        timer_counter = tk.Label(timer_frame, textvariable=self.current_time)
        timer_counter.grid(row=1, column=0, sticky="w")

        button_container = ttk.Frame(self, padding=10)
        button_container.grid(row=2, column=0, sticky="ew")
        # todo add buttons

        self.decrement_time()

    def decrement_time(self):
        current_time = self.current_time.get()
        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1
            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self.after(1000, self.decrement_time)

        elif self.timer_running and current_time == "00:00":
            self.timer_schedule.rotate(-1)
            next_up = self.timer_schedule[0]
            self.current_timer_label.set(next_up)
            if next_up == "Pomodoro":
                self.current_time.set("25:00")
            elif next_up == "Short Break":
                self.current_time.set("05:00")
            elif next_up == "long Break":
                self.current_time.set("15:00")
            self.after(1000, self.decrement_time)


root = PomodoroTimer()
root.mainloop()
