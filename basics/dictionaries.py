'''
    name : dictionaries.py
    Created by : Premal Upadhyay
    Date : 23-01-2022
'''

customer = {
    "name" : "Premal Upadhyay",
    "age" : 30,
    "is_verified" : True
}

print(customer["name"]) #accessing value associated with key with square brackets, you might get KeyError if key does'nt exist
print(customer.get("name", "Key does'nt exist")) #accessing value associated with key with get method, if key does'nt exist then it will return None
customer["birthdate"] = "1 Jan 1990" #adding new key to the dictionaries
print(customer.get("birthdate"))

#Excercise
phone = input("Phone : ")
number_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

output = ""
for number in phone:
    output += number_mapping.get(number, "!") + " " #Store the value associated with key in output string, it will return '!' if key does'nt value, appending space so that words are keep seperated
print(output)