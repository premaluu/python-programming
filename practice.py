'''
    name : practice.py
    Created by : Premal Upadhyay
    Date : 23-01-2022
'''

dict = {
    "name" : "Premal Upadhyay",
    "age" : "30",
    "is_verified" : True
}

print(f'Name : {dict["name"]}')
print(f'Age : {dict.get("age")}')
dict["birthdate"] = "1 Jan 2001"
print(dict.get("birthdate"))

#Excercise
numbers = input("Enter numbers :")
digit_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

for number in numbers:
    print(digit_mapping.get(number, "!"))