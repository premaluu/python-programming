'''
    name : for_loop.py
    Created by : Premal Upadhyay
    Date : 20-01-2022
'''

for item in 'Python':
    print(item)

for item in ['Premal', 'akshit', 'pratik', 'Meet']:
    print(item)

for item in range(5, 10, 2): #range(start, end, step)
    print(item)

total_cost = 0
prices = [10, 20, 30]

for price in prices:
    total_cost += price
print(f"Total cost : {total_cost}")