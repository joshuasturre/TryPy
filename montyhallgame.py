from random import randint
import time
while True:
    doorList = [0, 0 ,0]
    rand = randint(1, 3)
    if rand == 1:
        doorList[0] = 1
    if rand == 2:
        doorList[1] = 1
    if rand == 3:
        doorList[2] = 1
    print('Random data generated...: [*, *, *]')
    time.sleep(0.5)
    choice_init = int(input('Please choose a door: '))
    time.sleep(0.5)
    print('You have chosen door', choice_init)
    time.sleep(0.5)
    if choice_init == 1 and doorList[1] == 1:
        print('Door 2 has been opened, and it is EMPTY!!')
        if input('Would you like to switch? y/n') == 'y':
            choice_init = 3
    print(choice_init)
