import tkinter as tk
from PIL import Image, ImageTk


MOVE_PER_SPEED = 25
GAME_SPEED = 1000//MOVE_PER_SPEED


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)
        self.load_assets()
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)
        self.score = 0
        self.create_objects()
        self.after(GAME_SPEED, self.perform_actions)
    ################################################################

    def on_key_press(self, e):
        new_direction = e.keysym
        self.direction = new_direction

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]
        return (
            head_x_position in (0, 580) or head_y_position in (20, 600) or
            (head_x_position, head_y_position) in self.snake_positions[1:]
        )

    def move_snake(self):
        head_x_postion, head_y_position = self.snake_positions[0]
        if self.direction == "Left":
            new_head_position = (head_x_postion - 20, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_postion + 20, head_y_position)
        elif self.direction == "Down":
            new_head_position = (head_x_postion, head_y_position + 20)
        elif self.direction == "Up":
            new_head_position = (head_x_postion, head_y_position - 20)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)
    ###############################################################

    def perform_actions(self):
        if self.check_collisions():
            return

        self.move_snake()
        self.after(GAME_SPEED, self.perform_actions)
    ###############################################################

    def create_objects(self):
        self.create_text(
            45, 12, text=f"Score {self.score}", tag="score", fill="red", font=("TkDefaultFont", 14))
        self.create_rectangle(7, 27, 593, 613, outline="orange")
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position,
                              image=self.snake_body, tag="snake")

        self.create_image(
            *self.food_position, image=self.food_body, tag="food")
        # self.create_image(
        #     self.food_position[0], self.food_position[1], image=self.food_body, tag="food")

    def load_assets(self):
        try:
            self.snake_body_image = Image.open(
                "./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_body_image = Image.open(
                "./assets/food.png")
            self.food_body = ImageTk.PhotoImage(self.food_body_image)

        except Exception as ex:
            print(ex)


root = tk.Tk()
root.title('Snake')
root.resizable(False, False)
board = Snake()
board.pack()
root.mainloop()
