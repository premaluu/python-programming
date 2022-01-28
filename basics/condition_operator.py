'''
    name : logical_operator.py
    Created by : Premal Upadhyay
    Date : 17-01-2022
'''

temprature = 30

if temprature >= 30:
    print("It's hot day")
else:
    print("It's not hot day")

#Exercise
name = 'Premal'

if len(name) < 3:
    print("Name must be atleast 3 charcters")
elif len(name) > 50:
    print("Name can maximum of 50 characters")
else:
    print("Name looks good!")