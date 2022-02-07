'''
    name : class_basics.py
    Created by : Premal Upadhyay
    Date : 28-01-2022
'''


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(f'X : {point1.x} Y : {point1.y}')
point1.draw()

point2 = Point()
point2.x = 10
print(f'X : {point2.x}')
point2.draw()

"""
    --Exercise--
"""


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking')


person = Person("Premal")
person.talk()


class Basics:
    def __init__(self):
        print('Constructor is called.')

    def someMethod(self):
        print('In method body.')

    def __del__(self):
        print('In destructor.')


# Creating constructor
obj = Basics()

# Calling method of class
obj.someMethod()

# Calling destructor
del obj
