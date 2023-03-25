bitmap = '''..................................
              ******      
        *****************
..................................'''
message = input('> ')

for index, line in enumerate(bitmap.splitlines()):

    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[index % len(message)], end='')

    print()

# for line in bitmap.splitlines():
#     for i, bit in enumerate(line):
#         if bit == ' ':
#             print(' ', end='')
#         else:
#             print(message[i % len(message)], end='')

#     print()


#


# import turtle
# COLORS = ['red', 'green', 'blue', 'yellow', 'orange']
# s = turtle.Screen()
# p = turtle.Pen()
# p.shape('turtle')
# p.speed('fastest')  # 'fast'   'normal'   'slow'    'slowest'
# for j in range(12):
#     p.color(COLORS[j % len(COLORS)])
#     p.fillcolor(COLORS[j % len(COLORS)])
#     p.begin_fill()
#     for i in range(4):
#         p.forward(100)
#         p.left(90)
#     p.end_fill()

#     p.left(30)


# s.exitonclick()
