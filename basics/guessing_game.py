'''
    name : guessing_game.py
    Created by : Premal Upadhyay
    Date : 18-01-2022
'''

guess_limit = 3
guess_count = 1
secret_number = 9
while guess_count <= guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You're correct!")
        break
    guess_count += 1
else:
    print("Sorry, good luck next time :)")