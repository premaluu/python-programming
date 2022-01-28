'''
    name : list_method.py
    Created by : Premal Upadhyay
    Date : 23-01-2022
'''

list = [2, 2, 4, 6, 3, 4, 6, 1]

list.append(10) #append item at the end of list.
print(list)

list.insert(2, 15) #insert item at specific position
print(list)

list.remove(15) #removes particular element
print(list)

list.clear() #removes all elements
print(list)

list = [2, 2, 4, 6, 3, 4, 6, 1]

list.pop() #removes last element
print(list)

print(list.index(6)) #return index of specific item
print(6 in list) #finding whether item exist in the list or not

print(list.count(2)) #count the total occurance of given item

list.sort() #sort the list
print(list)

list.reverse() #reverse the list
print(list)

list_another = list.copy() #return the copy of list

#Exercise
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)