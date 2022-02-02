'''
    name : iterator.py
    Created by : Premal Upadhyay
    Date : 31-01-2022
'''

#Iterable
number_list = [1, 2, 3]

#Getting an interator.
value = iter(number_list)

#Fetching value one by one from that iterator object.
print(next(value))
print(next(value))
print(next(value))

#Iteration example
iter_obj = iter(number_list)

#This is how for loop iterate over iterable object under the hood.
while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break