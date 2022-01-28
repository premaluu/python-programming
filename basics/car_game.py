'''
    name : car_game.py
    Created by : Premal Upadhyay
    Date : 18-01-2022
'''

command = ''
started = False

while command != 'quit':
    command = input('>').lower()
    if command == 'start':
        if not started:
            print('Car started... Ready to go!')
            started = True
        else:
            print("Car already started.")
    elif command == 'stop':
        if started:
            print("Car stopped.")
            started = False
        else:
            print("Car already stopped.")
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand")