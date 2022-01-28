'''
    name : list.py
    Created by : Premal Upadhyay
    Date : 23-01-2022
'''

import numpy as np

names = ['John', 'Selena', 'Tony', 'Robert']
print(names) #accessing all elements
print(names[1]) #accessing single element
print(names[2:]) #accessing all elements after 2nd index
print(names[2:4]) #accessing elements between index 2-4

#Exercise
numbers = np.random.randint(1, 1000, 50) #This function return list of random elements from 1 to 1000 and it will return 50 random elements
print(numbers)
largest_number = numbers[0] #setting first element as largest element

for item in numbers:
    #Checking that previous largest number is
    if largest_number < item:
        largest_number = item

print(f"Largest number : {largest_number}")