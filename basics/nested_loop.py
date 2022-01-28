'''
    name : nested_loop.py
    Created by : Premal Upadhyay
    Date : 20-01-2022
'''

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#Exercise
numbers = [5, 2, 5, 2, 2]

for number in numbers:
    output = ''
    for stars in range(number):
        output += 'x'
    print(output)