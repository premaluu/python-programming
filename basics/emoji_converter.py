'''
    name : emoji_converter.py
    Created by : Premal Upadhyay
    Date : 24-01-2022
'''
message = input(">")
words = message.split(' ')
emoji = {
    ":)" : "😃",
    ":(" : "😔"
}

output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)