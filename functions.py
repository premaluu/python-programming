'''
    name : functions.py
    Created by : Premal Upadhyay
    Date : 24-01-2022
'''

#Function that greet the user
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

#Function that return square of number
def square(number):
    return number * number

print('Start')
print('Greeting the user')
greet_user(last_name='Smith', first_name='John')
print(f'Square of 3 is : {square(3)}')
print('Stop')