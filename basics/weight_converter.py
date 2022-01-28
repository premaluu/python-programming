'''
    name : weight_converter.py
    Created by : Premal Upadhyay
    Date : 18-01-2022
'''

weight = int(input("Weight: "))
weight_format = input("(L)bs or (K)G: ")

if weight_format.upper() == 'L':
    print(f"You are {weight*0.45} kg")
elif weight_format.upper() == 'K':
    print(f"You are {weight/0.45} pounds")