'''
    name : typeconversion.py
    Created by : Premal Upadhyay
    Date : 16-01-2022
'''
birth_year = input('Birth year : ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)

#Exercise
weight_in_lbs = input('Enter weight (in pounds) : ')
weight_in_kg = int(weight_in_lbs) * 0.45
print(weight_in_kg)