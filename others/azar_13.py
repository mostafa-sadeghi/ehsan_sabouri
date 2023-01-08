# class Things:
#     pass


# class Inanimate(Things):
#     pass


# class Animate(Things):
#     pass


# class Mammal(Animate):
#     def feed_young_with_milk(self):
#         pass


# class Animal(Animate):
#     def move(self):
#         pass

#     def eat(self):
#         pass


# animal = Animal()
# animal.eat()
# animal.move()
# print(type(animal))


# import turtle

# s = turtle.Screen()
# p = turtle.Pen()
# p.pencolor('red')
# for i in range(12):
#     for i in range(4):
#         p.forward(100)
#         p.left(90)
#     p.left(30)
# p.goto(100,100)
# #

# s.exitonclick()

class Person:
    name = ''
    family = ''

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def speak(self):
        print("speak")

    def learn(self):
        print("learn")


class Student(Person):
    def __init__(self):
        pass
        # super().__init__('', '')

    def go_to_school(self):
        print('go to school')


person1 = Person('ali', 'rezaei')
person1.speak()
student1 = Student()
student1.learn()
student1.go_to_school()

student2 = Student()
student2.speak()
