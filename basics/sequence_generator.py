'''
    name : sequence_generators.py
    Created by : Premal Upadhyay
    Date : 07-02-2022
'''


def generate_fibonacci():
    n1 = 0
    n2 = 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2


def generate_odd_numbers():
    no = 1

    while True:
        yield no
        no += 2