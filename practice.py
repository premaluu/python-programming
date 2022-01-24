'''
    name : practice.py
    Created by : Premal Upadhyay
    Date : 23-01-2022
'''

list = [2, 2, 4, 6, 7, 8]

list.append(10)
print(list)

list.insert(2, 3)
print(list)

list.remove(3)
print(list)

list.clear()
print(list)

list = [2, 2, 4, 6, 7, 8]
list.pop()
print(list)

print(list.count(2))

list.sort()
print(list)

list.reverse()
print(list)

print(list.copy())

print(list.index(2))
