'''
    name : condition.py
    Created by : Premal Upadhyay
    Date : 18-01-2022
'''

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink water")
elif is_cold:
    print("It's a cold day")
    print("Wear a warm clothes")
else:
    print("It's a lovely day")

#Excercise
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment : ${down_payment}")