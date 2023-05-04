import turtle


def my_func(x, y):
    # my_pen.stamp()
    # my_pen.forward(100)
    print(x, y)
    print(my_pen.position())


def my_drag_func(x, y):
    print("my_drag_func", (x, y))
    my_pen.goto(x, y)


my_pen = turtle.Turtle()
my_pen.speed('normal')  # 'fastest' 'fast' 'normal' 'slow' 'slowest'
my_pen.shape('turtle')
my_pen.penup()
# my_pen.goto(-50, 0)
# my_pen.pendown()
my_pen.color('red', 'green')
my_pen.pensize(4)


my_pen.home()
my_pen.begin_poly()
my_pen.fd(100)
my_pen.left(20)
my_pen.fd(30)
my_pen.left(60)
my_pen.fd(50)
my_pen.end_poly()
p = turtle.get_poly()
turtle.register_shape("myFavouriteShape", p)


# my_pen.shape("square")
# my_pen.shapesize(4,2)
# print(my_pen.get_shapepoly())

# my_pen.onclick(my_func)
# my_pen.ondrag(my_drag_func)

# my_pen.tilt(180)
# my_pen.shapesize(5, 5, 12)
# my_pen.setheading(180)
# my_pen.forward(100)
# my_pen.begin_fill()
# for i in range(5):
#     my_pen.forward(100)
#     my_pen.right(144)
# my_pen.end_fill()

# my_pen.penup()
# my_pen.setpos(100, 200)  # my_pen.setposition(-70,200)
# my_pen.write('Our Nice Star', font=("Arial", 20, 'bold'))

# my_pen.hideturtle()

turtle.done()
