'''
    name : generators.py
    Created by : Premal Upadhyay
    Date : 07-02-2022
'''

from sequence_generator import *


def generator_even_numbers(max):
    no = 2

    while no <= max:
        yield no
        no += 2


# This statement will return generator which is iterator
numbers = generator_even_numbers(6)

print(next(numbers))  # 2
print(next(numbers))  # 4
print(next(numbers))  # 6

# Generating infinite fibonacci
fibonacci_numbers = generate_fibonacci()

for numbers in range(1, 100):
    print(next(fibonacci_numbers), end=" ")

print()

# Generating a lot of odd numbers
odd_numbers = generate_odd_numbers()

for numbers in range(1, 100):
    print(next(odd_numbers), end=" ")