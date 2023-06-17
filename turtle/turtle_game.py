from turtle import Screen, Turtle

display_surface = Screen()
display_surface.bgcolor('blue')
display_surface.title('Snake Game')
display_surface.setup(width=600, height=600)

root = display_surface._root
root.resizable(False, False)

root.iconbitmap('images\orange.ico')


running = True
while running:
    display_surface.update()
