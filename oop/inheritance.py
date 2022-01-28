'''
    name : inheritance.py
    Created by : Premal Upadhyay
    Date : 28-01-2022
'''


class Memmel:
    def walk(self):
        print("Walk")


class Dog(Memmel):
    def bark(self):
        print('Bark')


class Cat(Memmel):
    def meow(self):
        print('Meow')


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.meow()