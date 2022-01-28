'''
    name : logical_operator.py
    Created by : Premal Upadhyay
    Date : 18-01-2022
'''

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

has_criminal_record = True

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")