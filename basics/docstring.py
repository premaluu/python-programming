'''
    name : docstring.py
    Created by : Premal Upadhyay
    Date : 03-03-2022
'''


def add(a, b):
    """
    This function is used to add two numbers

    :param a: first operand for addition
    :param b: second operand for addition
    :return: returns addition of a and b
    """
    #Prints doc comments
    print(add.__doc__)
    return a + b


print(add(10, 15))
