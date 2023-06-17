import tkinter as tk
from PIL import Image, ImageTk
import random

MOVE_PER_SPEED = 25
GAME_SPEED = 1000//MOVE_PER_SPEED


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)
        self.load_assets()
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_position()
        self.score = 0
        self.create_objects()
        self.after(GAME_SPEED, self.perform_actions)
    ################################################################

    def on_key_press(self, e):
        new_direction = e.keysym
        opposites = ({"Up", "Down"}, {"Right", "Left"})
        if {new_direction, self.direction} not in opposites:
            self.direction = new_direction

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]
        return (
            head_x_position in (0, 580) or head_y_position in (20, 600) or
            (head_x_position, head_y_position) in self.snake_positions[1:]
        )

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag("food"), self.food_position)
            self.score += 1
            score = self.find_withtag('score')
            self.itemconfigure(score, text=f"Score: {self.score}", tag="score")
            self.snake_positions.append(self.snake_positions[-1])
            self.create_image(*self.snake_positions[-1],
                              image=self.snake_body, tag="snake")

    def set_new_food_position(self):
        while True:
            x_position = random.randint(1, 20) * 20
            y_position = random.randint(3, 22) * 20
            food_position = (x_position, y_position)
            if food_position not in self.snake_positions:
                return food_position

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
            self.end_game()
            return
        self.check_food_collision()
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

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(self.winfo_width()/2, self.winfo_height()/2,
                         text=f"Game over ! Your score:{self.score}", fill="#fff", font=('TkDefaultFont', 24))


root = tk.Tk()
root.title('Snake')
root.resizable(False, False)
board = Snake()
board.pack()
root.mainloop()
