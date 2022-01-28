'''
    name : list_method.py
    Created by : Premal Upadhyay
    Date : 28-01-2022
'''

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid Integer input.')