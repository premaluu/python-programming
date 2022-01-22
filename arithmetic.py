'''
    name : arithmetic.py
    Created by : Premal Upadhyay
    Date : 17-01-2022
'''

import math

print(10 + 5) #addition
print(10 - 5) #subtraction
print(10 * 5) #multiplication
print(10 / 5) #division
print(10 ** 5) #exponent
print(10 % 5) #modulo

# Augmented assignment operator
x = 10
x += 3
print(x)

# Operator precedence
x = (10 + 3) * 2 ** 5 #45
print(x)

#Math functions
print(round(3.6)) #4
print(abs(-3.5)) #3.5
print(math.ceil(3.6)) #4
print(math.floor(3.6)) #3