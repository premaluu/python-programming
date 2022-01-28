'''
    name : emoji_converter_function.py
    Created by : Premal Upadhyay
    Date : 28-01-2022
'''


def convert_emoji(message):
    words = message.split(' ')
    emoji = {
        ":)": "😃",
        ":(": "😔"
    }

    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input(">")
print(convert_emoji(message))
