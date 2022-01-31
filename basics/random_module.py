'''
    name : random_module.py
    Created by : Premal Upadhyay
    Date : 31-01-2022
'''

import random

# fetching random value
print(random.random())

# fetching random value between specific range
print(random.randint(5, 8))

# choose random value from list
list = ['Premal', 'Pratik', 'Prince', 'Priyank']
print(random.choice(list))


# Exercise

class Dice:
    def roll(self):
        """
        This function will generate random dice.

        :return: A tuple containing random dice value
        """
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
