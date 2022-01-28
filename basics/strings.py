'''
    name : strings.py
    Created by : Premal Upadhyay
    Date : 16-01-2022
'''

course = 'Python course for beginners'
copy = course[:]
print(course)
print(copy)
print(course[0:-1])
print(course[-1])
print(course[0:-4])
print(course[5:-1])

#Formatted string
first = 'John'
last = 'Wick'
message = first + ' <' + last + '> is a master.'
msg = f'{first} <{last}> is a master.'
print(message)
print(msg)

#String function
course_name = 'Python for beginners'
print(len(course_name)) #Return the length of string

'''
    upper() method returns the uppercase of given string
    NOTE : It will not change the original string, it will return another string which is converted to upper case.
'''
print(course_name.upper())
'''
    lower() method returns the lowercase of given string
    NOTE : It will not change the original string, it will return another string which is converted to lower case.
'''
print(course_name.lower())

'''
    find() method find the first occurance of character in the string.
    NOTE : In case if we try to find word or sequence of character then it will return the position from where the word is starting in the string.
'''
print(course_name.find('o'))
print(course_name.find('beginners'))

'''
    replace() method replaces the character or character sequence with another character or character sequence in string
'''
print(course_name.replace('beginners', 'Absolute beginners'))
print(course_name.replace('P', 'J'))
'''
    in operators return true/false based on existence of character sequence in the string.
'''
print('beginners' in course_name)

#Exercise
name = 'Jenifer'
print(name[1:-1]) #Guess the output of this statement