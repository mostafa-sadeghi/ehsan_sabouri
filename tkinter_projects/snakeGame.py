import tkinter as tk
from PIL import Image, ImageTk


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)
        self.load_assets()

    def load_assets(self):
        try:
            self.snake_body_image = Image.open(
                "./tkinter_projects/assets/snake.png")
            self.snake_body = ImageTk(self.snake_body_image)

            self.food_body_image = Image.open(
                "./tkinter_projects/assets/food.png")
            self.food_body = ImageTk(self.snake_food_image)

        except:
            print("file not found")


root = tk.Tk()
root.title('Snake')
root.resizable(False, False)
board = Snake()
board.pack()
root.mainloop()
