'''
    Module name : utils.py
    Created by : Premal Upadhyay
    Date : 28-01-2022
'''

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if maximum < number:
            maximum = number
    return maximum